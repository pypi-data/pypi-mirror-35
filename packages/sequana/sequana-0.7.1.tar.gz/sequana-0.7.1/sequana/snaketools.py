# -*- coding: utf-8 -*-
#
#  This file is part of Sequana software
#
#  Copyright (c) 2016 - Sequana Development Team
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#      Dimitri Desvillechabrol <dimitri.desvillechabrol@pasteur.fr>,
#          <d.desvillechabrol@gmail.com>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/sequana/sequana
#  documentation: http://sequana.readthedocs.io
#
##############################################################################
"""Set of tools to manipulate Snakefile and config files

Here is an overview (see details here below)

.. autosummary::
    :nosignatures:

    sequana.snaketools.DOTParser
    sequana.snaketools.FastQFactory
    sequana.snaketools.FileFactory
    sequana.snaketools.Module
    sequana.snaketools.ModuleFinderSingleton
    sequana.snaketools.PipelineManager
    sequana.snaketools.SnakeMakeStats
    sequana.snaketools.SequanaConfig
    sequana.snaketools.message
    sequana.snaketools.modules


"""
import os
import re
import json
import glob
import shutil
import warnings

import easydev
from easydev import get_package_location as gpl
from easydev import load_configfile, AttrDict, TempFile

import ruamel.yaml
from ruamel.yaml import comments

from sequana.misc import wget
from sequana import sequana_data, logger
from sequana.errors import SequanaException

from sequana import logger

__all__ = ["DOTParser", "FastQFactory", "FileFactory",
           "Module", "PipelineManager", "SnakeMakeStats",
           "SequanaConfig", "modules", "pipeline_names"]

try:
    # This is for python2.7
    import snakemake
except:
    logger.warning("Snakemake must be installed. Available for Python3 only")
    class MockSnakeMake(object):
        def __init__(self):
            pass

        def Workflow(self, filename):
            raise ImportError
    snakemake = MockSnakeMake()


class SnakeMakeStats(object):
    """Interpret the snakemake stats file

    Run the Snakemake with this option::

        -- stats stats.txt

    Then:

    .. plot::
        :include-source:

        from sequana.snaketools import SnakeMakeStats
        from sequana import sequana_data
        filename = sequana_data("test_snakemake_stats.txt", "testing")
        s = SnakeMakeStats(filename)
        s.plot()

    """
    def __init__(self, filename, N=1):
        """.. rubric:: Cosntructor"""
        self.filename = filename
        self.N = N

    def _parse_data(self):
        with open(self.filename, 'r') as fin:
            data = json.load(fin)
        return data

    def plot(self, fontsize=16):
        """Create the barplot from the stats file"""
        from sequana.lazy import pylab
        from sequana.lazy import pandas as pd
        pylab.clf()
        df = pd.DataFrame(self._parse_data()['rules'])
        ts = df.ix['mean-runtime']
        total_time = df.ix['mean-runtime'].sum()
        #ts['total'] = self._parse_data()['total_runtime'] / float(self.N)
        ts['total'] = total_time
        ts.sort_values(inplace=True)

        ts.plot.barh(fontsize=fontsize)
        pylab.grid(True)
        pylab.xlabel("Seconds (s)", fontsize=fontsize)
        try:
            pylab.tight_layout()
        except:
            pass

    def plot_and_save(self, filename="snakemake_stats.png",
                      outputdir="report"):
        import pylab
        # If the plot cannot be created (e.g. no valid stats), we create an empty
        # axes
        try: self.plot()
        except:
            pylab.bar([0],[0])
        if outputdir is None:
            pylab.savefig(filename)
        else:
            pylab.savefig(outputdir + os.sep + filename)


def plot_stats(inputdir=".", outputdir=".",
               filename="snakemake_stats.png", N=1):
    logger.info("Workflow finished. Creating stats image")
    try:
        SnakeMakeStats("%s/stats.txt" % inputdir, N=N).plot_and_save(
            outputdir=outputdir, filename=filename)
    except Exception as err:
        logger.error(err)
        logger.error("Could not process %s/stats.txt file" % inputdir)


class ModuleFinderSingleton(object):
    """Data structure to hold the :class:`Module` names"""
    def __init__(self):
        """.. rubric:: constructor

        :param list extra_paths:

        .. doctest::

            >>> from sequana import ModuleFinderSingleton
            >>> modnames = ModuleFinderSingleton()
            >>> modnames.isvalid('dag')
            True
            >>> modnames.isvalid('dummy')
            False

        """
        # names for each directory
        self._paths = {}
        self._type = {}

        # scan the official paths
        self._add_names("rules")
        self._add_names("pipelines")

    def _add_names(self, path):
        sepjoin = os.sep.join
        fullpath = sepjoin([gpl("sequana"), "sequana", path])

        fullpaths = self._iglob(fullpath)
        for this in fullpaths:
            whatever, module_name, filename = this.rsplit(os.sep, 2)
            if module_name in self._paths.keys():
                raise ValueError("Found duplicated name %s. "
                                 "Overwrites previous rule " % module_name)
            self._paths[module_name] = whatever + os.sep + module_name
            self._type[module_name] = path[:-1]

    def _iglob(self, path, extension="rules"):
        try:
            from glob import iglob
            matches = tuple(iglob("%s/**/*.%s" % (path, extension),
                                 recursive=True))
        except:
            # iglob use recursivity with ** only in py3.5 (snakemake)
            import fnmatch
            import os
            matches = []
            for root, dirnames, filenames in os.walk(path):
                for filename in fnmatch.filter(filenames, '*.' + extension):
                    matches.append(os.path.join(root, filename))
        return matches

    def _get_names(self):
        return sorted(list(self._paths.keys()))
    names = property(_get_names, doc="list of existing module names")

    def isvalid(self, name):
        """Check that a name is an existing and valid module"""
        if name not in self.names:
            return False
        return True

    def is_pipeline(self, name):
        return self._type[name] == "pipeline"

moduleFinder = ModuleFinderSingleton()


class Module(object):
    """Data structure that holds metadata about a **Module**

    In Sequana, we provide rules and pipelines to be used with snakemake.
    Snakemake rules look like::

        rule <name>:
            :input: file1
            :output: file2
            :shell: "cp file1 file2"

    A pipeline may look like::

        include: "path_to_rule1"
        include: "path_to_rule2"
        rule all:
            input: FINAL_FILES

    Note that the pipeline includes rules by providing the path to them.

    All rules can be stored in a single directory. Similarly for pipelines.
    We decided not to use that convention. Instead, we bundle rules (and
    pipelines) in their own directories so that other files can be stored
    with them. We also consider that

        #. if the **Snakefile** includes other **Snakefile** then
           it is **Pipeline**.
        #. Otherwise it is a simple **Rule**.

    So, a **Module** in sequana's parlance is a directory that contains a
    rule or a pipeline and associated files. There is currently no strict
    conventions for rule Modules except for their own rule file. However,
    pipeline Modules should have the following files:

        - A **snakemake** file named after the directory with the extension
          **.rules**
        - A **README.rst** file in restructured text format
        - An optional config file in YAML format named config.yaml.
          Although json format is possible, we use YAML throughout
          **sequana** for consistency. Rules do not have any but pipelines
          do. So if a pipeline does not provide a config.yaml, the one found
          in ./sequana/sequana/pipelines will be used.
        - a **requirements.txt**

    .. note:: Developers who wish to include new rules should refer to the
        Developer guide.

    .. note:: it is important that module's name should be used to name
        the directory and the rule/pipeline.

    The **Modules** are stored in sequana/rules and sequana/pipelines
    directories. The modules' names cannot be duplicated.

    Example::

        pipelines/test_pipe/test_pipe.rules
        pipelines/test_pipe/README.rst
        rules/rule1/rule1.rules
        rules/rule1/README.rst

    The :class:`Module` will ease the retrieval of information linked to a
    rule or pipeline. For instance if a pipeline has a config file, its path
    can be retrived easily::

        m = Module("quality_control")
        m.config

    This Module may be rule or pipeline, the method :meth:`is_pipeline` can
    be used to get that information. Other useful methods are available such
    as :meth:`onweb` that open the web page of the pipeline (linked to the
    README).

    """
    def __init__(self, name):
        """.. rubric:: Constructor

        :param str name: the name of an available module.

        """
        self._mf = moduleFinder
        self._mf.isvalid(name)

        if name not in self._mf.names:
            raise ValueError("""Sequana error: unknown rule or pipeline. Check
the source code at:

    https://github.com/sequana/sequana/tree/develop/sequana/pipelines and
    https://github.com/sequana/sequana/tree/develop/sequana/rules

or open a Python shell and type::

    import sequana
    sequana.modules.keys()""")
        else:
            self._path = self._mf._paths[name]

        self._name = name

        # could look into ./rules or ./pipelines
        self._snakefile = None
        self._description = None
        self._requirements = None

    def is_pipeline(self):
        """Return true is this module is a pipeline"""
        return self._mf.is_pipeline(self._name)

    def _get_file(self, name):
        filename = self._path + os.sep + name
        if os.path.exists(filename):
            return filename

    def __repr__(self):
        str = "Name: %s\n" % self._name
        str += "Path: %s\n" % self.path
        str += "Config: %s\n" % self.config
        str += "Cluster config: %s\n" % self.cluster_config
        str += "Schema for config file: %s\n" % self.schema_config
        return str

    def __str__(self):
        txt = "Rule **" + self.name + "**:\n" + self.description
        return txt

    def _get_path(self):
        return self._path
    path = property(_get_path, doc="full path to the module directory")

    def _get_config(self):
        # The default config file for that module
        filename = self._get_file("config.yaml")
        if filename is None:
            # or the sequana default config file
            filename = self._get_file("../config.yaml")
        return filename
    config = property(_get_config,
                      doc="full path to the config file of the module")

    def _get_schema_config(self):
        # The default config file for that module
        filename = self._get_file("schema.yaml")
        if filename is None:
            # or the sequana default config file
            filename = self._get_file("../schema.yaml")
        return filename
    schema_config = property(_get_schema_config,
                      doc="full path to the schema config file of the module")

    def _get_cluster_config(self):
        # The default config file for that module
        return self._get_file("cluster_config.json")
    cluster_config = property(_get_cluster_config,
                      doc="full path to the config cluster file of the module")

    def _get_readme(self):
        return self._get_file("README.rst")
    readme = property(_get_readme,
                      doc="full path to the README file of the module")

    def _get_overview(self):
        result = "no information. For developers: please fix the pipeline "
        result += "README.rst file by adding an :Overview: field"
        for this in self.description.split("\n"):
            if this.startswith(':Overview:'):
                try:
                    result = this.split(":Overview:")[1].strip()
                except:
                    result += "Bad format in :Overview: field"
        return result
    overview = property(_get_overview)

    def _get_snakefile(self):
        if self._snakefile is not None:
            return self._snakefile

        if self._get_file("Snakefile"):
            self._snakefile = self._get_file("Snakefile")
        elif self._get_file("Snakefile." + self.name):
            self._snakefile = self._get_file("Snakefile." + self.name)
        elif self._get_file(self.name + '.rules'):
            self._snakefile = self._get_file(self.name + ".rules")
        else:
            print("//Snakefile for %s not found" % self.name)
        return self._snakefile
    snakefile = property(_get_snakefile,
                         doc="full path to the Snakefile file of the module")

    def _get_name(self):
        return self._name
    name = property(_get_name, doc="name of the module")

    def _get_requirements(self):
        if self._requirements is not None:
            return self._requirements
        if self._get_file("requirements.txt"):
            self._requirements = self._get_file("requirements.txt")
            return self._requirements
    requirements = property(_get_requirements, doc="list of requirements")

    def is_executable(self, verbose=False):
        """Is the module executable

        A Pipeline Module should have a requirements.txt file that is
        introspectied to check if all executables are available;

        :param verbose:
        :return: a tuple. First element is a boolean to tell if it executable.
            Second element is the list of missing executables.
        """
        if self.requirements is None:
            return True, []

        executable = True
        missing = []

        # reads the file and interpret it to figure out the
        # executables/packages and pipelines required
        pipelines = []
        with open(self.requirements, "r") as fh:
            data = fh.read()
            datalist = [this.strip() for this in data.split("\n")
                        if this.strip() not in [""]]
            reqlist = []
            for this in datalist:
                if this.startswith('-'):
                    req = this.split("-")[1].split()[0].strip()
                    if req.startswith("["):
                        req = req.replace("[", "")
                        req = req.replace("]", "")
                        pipelines.append(req)
                    else:
                        reqlist.append(req)

        # Check the pipelines independently
        for pipeline in pipelines:
            Module(pipeline).check()

        for req in reqlist:
            # It is either a Python package or an executable
            try:
                easydev.shellcmd("which %s" % req)
                if verbose:
                    print("Found %s executable" % req)
            except:
                # is this a Python code ?
                if len(easydev.get_dependencies(req)) == 0:
                    if verbose:
                        print("%s not found !!" % req)
                    executable = False
                    missing.append(req)
                else:
                    if verbose:
                        print("%s python package" % req)
        return executable, missing

    def check(self, mode="warning"):
        executable, missing = self.is_executable(verbose=False)
        if executable is False:
            _  = self.is_executable(verbose=True)
            txt = "Some executable or Python packages are not available:\n"
            txt += "Some functionalities may not work "
            if mode == "warning":
                print(txt)
            elif mode == "error":
                txt += "Use \n conda install missing_package_name;"
                for this in missing:
                    txt += "- %s\n" % this
                raise ValueError(txt)

    def _get_description(self):
        try:
            with open(self.readme) as fh:
                self._description = fh.read()
        except:
                self._description = "no description"
        return self._description
    description = property(_get_description,
                           doc=("Content of the README file associated with "))
    def onweb(self):
        # TOD: automatic switch
        if "rules" in self._path:
            suffix = self.snakefile.split("rules/")[1]
            suffix = suffix.rsplit("/", 1)[0]
            easydev.onweb("http://github.com/sequana/sequana/tree/"
                  "master/sequana/rules/%s" % suffix)
        else:
            suffix = self.snakefile.split("pipelines/")[1]
            suffix = suffix.rsplit("/", 1)[0]
            easydev.onweb("http://github.com/sequana/sequana/tree/"
                  "master/sequana/pipelines/%s" % self.name)

    def md5(self):
        """return md5 of snakefile and its default configuration file

        ::

            >>> from sequana import snaketools as sm
            >>> m = sm.Module("variant_calling")
            >>> m.md5()
            {'config': 'e23b26a2ff45fa9ddb36c40670a8a00e',
             'snakefile': '7d3917743a6b123d9861ddbbb5f3baef'}

        """
        data = {}
        data["snakefile"] = easydev.md5(self.snakefile)
        data["config"] = easydev.md5(self.config)
        return data


def _get_modules_snakefiles():
    modules = {}
    for name in moduleFinder.names:
        module = Module(name)
        filename = module.snakefile
        if filename:
            modules[name] = filename
    return modules

# dictionary with module names as keys and fullpath to the Snakefile as values
modules = _get_modules_snakefiles()

#: list of pipeline names found in the list of modules
pipeline_names = [m for m in modules if Module(m).is_pipeline()]


class SequanaConfig(object):
    """Reads YAML config file and ease access to its contents

    This can also be used to check the validity of the config file

    ::

        >>> sc = SequanaConfig(config)
        >>> sc.config.pattern == "*.fastq.gz"
        True

    Input files should be stored into::

        input_samples:
            - file1: FILE1
            - file2: FILE2

    The second file may be optional.


    Empty strings in a config are interpreted as None but SequanaConfig will
    replace  None with empty strings, which is probably what was expected from
    the user. Similarly, in snakemake when settings the config file, one
    can override a value with a False but this is interepted as "False"
    This will transform back the "True" into True.

    Another interest concerns the automatic expansion of the path to directories
    and files starting with the special ~ (tilde) character, that are expanded
    transparently.


    """
    def __init__(self, data=None, converts_none_to_str=True):
        """Could be a JSON or a YAML file

        :param str filename: filename to a config file in json or YAML format.

        SEQUANA config files must have some specific fields::

            input_directory
            input_samples...
        """
        # Create a dummy YAML code to hold data in case the input is a json
        # or a dictionary structure. We use a CommentedMap that works like
        # a dictionary. Be aware that the update method will lose the comments
        if data is None:
            self.config = AttrDict()
            self._yaml_code = comments.CommentedMap()
        elif isinstance(data, str): # else is it a filename ?
            if os.path.exists(data):
                if data.endswith(".yaml") or data.endswith(".yml"):
                    with open(data, "r") as fh:
                        self._yaml_code = ruamel.yaml.load(
                            fh.read(), ruamel.yaml.RoundTripLoader)
                else:
                    # read a JSON
                    import yaml
                    with open(data, "r") as fh:
                        self._yaml_code =  yaml.load(json.dumps(
                            json.loads(fh.read())))
                config = load_configfile(data)
            else:
                raise IOError("input string must be an existing file (%s)" % data)
            self.config = AttrDict(**config)
        elif isinstance(data, SequanaConfig): # else maybe a SequanaConfig ?
            self.config = AttrDict(**data.config)
            self._yaml_code = comments.CommentedMap(self.config.copy())
        else: # or a pure dictionary ?
            self.config = AttrDict(**data)
            self._yaml_code = comments.CommentedMap(self.config.copy())
        self.cleanup_config()

    def check_sequana_fields(self):
        requirements = ["input_directory",
                        "input_samples",
                        "input_extension",
                        "input_pattern",
                        "input_samples:file1", "input_samples:file2"]
        # converts to dictionary ?
        for this in requirements:
            this = this.split(":")[0]
            if this not in self.config.keys():
                return False
        return True

    def save(self, filename="config.yaml", cleanup=True):
        """Save the yaml code in _yaml_code with comments"""
        # This works only if the input data was a yaml
        if cleanup:
            self.cleanup() # changes the config and yaml_code to remove %()s

        # get the YAML formatted code and save it
        newcode = ruamel.yaml.dump(self._yaml_code,
                    Dumper=ruamel.yaml.RoundTripDumper,
                    default_style="", indent=4, block_seq_indent=4)

        # Finally, save the data
        with open(filename, "w") as fh:
            fh.write(newcode)

    def _recursive_update(self, target, data):
        # recursive update of target using data. Both target and data must have
        # same items
        for key, value in data.items():
            if isinstance(value, dict):
                target[key] = comments.CommentedMap(
                    self._recursive_update(target[key], data[key]))
            else:
                #print(target)
                if key in target.keys():
                    target[key] = value
                else:
                    logger.warning("This %s key was not in the original config"
                                   " but added" % key)
        return target

    def _update_yaml(self):
        self._recursive_update(self._yaml_code, self.config)

    def _update_config(self):
        self._recursive_update(self.config, self._yaml_code)

    def _recursive_cleanup(self, d):
        # expand the tilde (see https://github.com/sequana/sequana/issues/486)
        # remove the %() templates
        for key, value in d.items():
            try:
                self._recursive_cleanup(value)
            except AttributeError:
                if value is None:
                    d[key] = ""
                elif isinstance(value, str):
                    if value.startswith('%('):
                        d[key] = None
                    else:
                        d[key] = value.strip()
                    # https://github.com/sequana/sequana/issues/486
                    if key.endswith("_directory") and value.startswith("~/"):
                        d[key] = os.path.expanduser(value)
                    if key.endswith("_file") and value.startswith("~/"):
                        d[key] = os.path.expanduser(value)

    def cleanup_config(self):
        self._recursive_cleanup(self.config)
        self._update_yaml()

    def cleanup(self):
        """ Remove template elements and change None to empty string.
        """
        self._recursive_cleanup(self._yaml_code)
        self._update_config()

    def copy_requirements(self, target):
        """Copy files to run the pipeline

        If a requirement file exists, it is copied in the target directory.
        If not, it can be either an http resources or a sequana resources.

        """
        if 'requirements' in self._yaml_code.keys():
            for requirement in self._yaml_code['requirements']:
                if os.path.exists(requirement):
                    try:
                        shutil.copy(requirement, target)
                    except:
                        pass # the target and input may be the same
                elif requirement.startswith('http') is False:
                    try:
                        logger.info('Copying %s from sequana' % requirement)
                        shutil.copy(sequana_data(requirement), target)
                    except:
                        logger.warning("This requirement %s was not found in "
                                       " sequana.")
                elif requirement.startswith("http"):
                    logger.info("This file %s will be needed. Downloading" %
                                requirement)
                    output = requirement.split("/")[-1]
                    wget(requirement, target + os.sep + output)

    def check_config_with_schema(self, schemafile):
        """Check the config file with respect to a schema file

        Sequana pipelines should have a schema file in the Module.

        """
        from pykwalify.core import Core
        # causes issue with ruamel.yaml 0.12.13. Works for 0.15
        warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
        try:
            # open the config and the schema file
            with TempFile(suffix=".yaml") as fh:
                self.save(fh.name)
                c = Core(source_file=fh.name, schema_files=[schemafile])
        except Exception as err:
            print(err)
            return False


class DummyManager(object):
    def __init__(self, filenames=None, samplename="custom"):
        self.config = {}
        if isinstance(filenames, list) and len(filenames) == 2:
            self.paired = True
            self.samples = {samplename: filenames}
        elif isinstance(filenames, list) and len(filenames) == 1:
            self.paired = False
            self.samples = {samplename: filenames}
        elif isinstance(filenames, str):
            self.samples = {samplename: [filenames]}
            self.paired = False


class PipelineManager(object):
    """Utility to manage easily the snakemake pipeline

    Inside a snakefile, use it as follows::

        from sequana import PipelineManager
        manager = PipelineManager("pipeline_name", "config.yaml")

    config file must have these fields::

        - input_directory:  #a_path
        - input_extension:  fastq.gz  # this is the default. could be also fq.gz
        - input_readtag: _R[12]_ # default
        - input_pattern:    # a_global_pattern e.g. H*fastq.gz
        - input_samples:
            - file1:
            - file2:

    The manager can then easily access to the data with a :class:`FastQFactory`
    instance::

        manager.ff.filenames

    This can be further used to get a wildcards with the proper directory.

    The manager also tells you if the samples are paired or not assuming all
    samples are homogneous (either all paired or all single-ended).

    If there is only one sample, the attribute :attr:`mode` is set to "nowc"
    meaning no wildcard. Otherwise, we assume that we are in a wildcard mode.

    When the mode is set, two attributes are also set: :attr:`sample` and
    :attr:`basename`.

    If the mode is **nowc**, the *sample* and *basename* are hardcoded to
    the sample name and  sample/rule/sample respectively. Whereas in the
    **wc** mode, the sample and basename are wildcard set to "{sample}"
    and "{sample}/rulename/{sample}". See the following methods :meth:`getname`.

    For developers: the config attribute should be used as getter only.

    """
    def __init__(self, name, config, pattern="*.fastq.gz", fastq=True):
        """.. rubric:: Constructor

        :param name: name of the pipeline
        :param config:  name of a configuration file
        :param pattern: a default pattern if not provided in the configuration
            file as an *input_pattern* field.
        """
        cfg = SequanaConfig(config)
        cfg.config.pipeline_name = name
        self.pipeline_dir = os.getcwd() + os.sep

        # Default mode is the input directory .
        if "input_directory" not in cfg.config.keys():
            self.error("input_directory must be found in the config.yaml file")

        # First, one may provide the input_directory field
        if cfg.config.input_directory:
            directory = cfg.config.input_directory.strip()
            if os.path.isdir(directory) is False:
                self.error("The (%s) directory does not exist." % directory)

            if "input_extension" in cfg.config.keys() and \
                    cfg.config['input_extension'] not in (None, ""):
                glob_dir = directory + os.sep + "*" + \
                           cfg.config['input_extension']
            else:
                glob_dir = directory + os.sep + pattern
        # otherwise, the input_pattern can be used
        elif cfg.config.input_pattern:
            glob_dir = cfg.config.input_pattern
        # otherwise file1
        elif cfg.config.input_samples['file1']:
            glob_dir = [cfg.config.input_samples['file1']]
            if cfg.config.input_samples['file2']:
                glob_dir += [cfg.config.input_samples['file2']]
        # finally, if none were provided, this is an error
        else:
            self.error("No valid input provided in the config file")

        logger.debug("Input data{}".format(glob_dir))

        if not cfg.config.input_readtag:
             cfg.config.input_readtag = "_R[12]_"

        if fastq:
            self._get_fastq_files(glob_dir, cfg.config.input_readtag)
        else:
            self._get_bam_files(glob_dir)
        # finally, keep track of the config file
        self.config = cfg.config

    def _get_fastq_files(self, glob_dir, read_tag):
        """

        """
        self.ff = FastQFactory(glob_dir, read_tag=read_tag)
        if self.ff.filenames == 0:
            self.error("No files were found with pattern %s and read tag %s.".format(glob_dir, read_tag))

        # change [12] regex
        rt1 = read_tag.replace("[12]", "1")
        rt2 = read_tag.replace("[12]", "2")

        # count number of occurences
        R1 = [1 for this in self.ff.filenames if rt1 in this]
        R2 = [1 for this in self.ff.filenames if rt2 in this]

        if len(R2) == 0:
            self.paired = False
        else:
            if R1 == R2:
                self.paired = True
            else:
                raise ValueError("Mix of paired and single-end data sets not "
                                 "implemented yet")

        # Note, however, that another mode is the samples.file1/file2 . If
        # provided, filenames is not empty and superseeds
        # the previous results (with the glob). Here only 2 files are provided
        # at most
        if not self.ff:
            filenames = self._get_filenames(cfg.config)
            if len(filenames):
                self.ff = FastQFactory(filenames)
                if len(filenames) == 2:
                    self.paired = True
                else:
                    self.paired = False

        ff = self.ff  # an alias
        self.samples = {tag: [ff.get_file1(tag), ff.get_file2(tag)]
                        if ff.get_file2(tag) else [ff.get_file1(tag)]
                        for tag in ff.tags}

        if len(ff.tags) == 0:
            raise ValueError("Could not find fastq.gz files with valid format "
                             "(NAME_R1_<SUFFIX>.fastq.gz where <SUFFIX> is "
                             "optional")
        else:
            self.sample = "{sample}"
            self.basename = "{sample}/%s/{sample}"

    def _get_bam_files(self, pattern):
        ff = FileFactory(pattern)
        self.samples = {tag: fl for tag, fl in zip(ff.filenames, ff.realpaths)}
        self.sample = "{sample}"
        self.basename = "{sample}/%s/{sample}"

    def error(self, msg):
        msg += ("\nPlease check the content of your config file. You must have "
                "input_directory set, or input_pattern, or input_samples:file1 "
                "(and optionally input_samples:file2).")
        raise SequanaException(msg)

    def getname(self, rulename, suffix=None):
        """In the basename, include rulename and suffix"""
        if suffix is None:
            suffix = ""
        return self.basename % rulename + suffix

    def getreportdir(self, acronym):
        """Create the report directory.
        """
        return "{1}{0}report_{2}_{1}{0}".format(os.sep, self.sample, acronym)

    def getwkdir(self, rulename):
        return self.sample + os.sep + rulename + os.sep

    def getlogdir(self, rulename):
        """ Create log directory: */sample/logs/sample_rule.logs
        """
        return "{1}{0}logs{0}{1}.{2}.log".format(os.sep, self.sample, rulename)

    def getrawdata(self):
        """Return list of raw data

        If :attr:`mode` is *nowc*, a list of files is returned (one or two files)
        otherwise, a function compatible with snakemake is returned. This function
        contains a wildcard to each of the samples found by the manager.
        """
        return lambda wildcards: self.samples[wildcards.sample]

    def _get_filenames(self, cfg):
        filenames = []
        file1 = cfg.samples.file1
        file2 = cfg.samples.file2
        if file1:
            if os.path.exists(file1):
                filenames.append(file1)
            else:
                raise FileNotFoundError("%s not found" % file1)
        if file2:
            if os.path.exists(file2):
                filenames.append(file2)
            else:
                raise FileNotFoundError("%s not found" % file2)
        return filenames

    def message(self, msg):
        message(msg)


def message(mes):
    """Dedicated print function to include in Snakefiles

    In a Snakefile, the stand print function may interfer with other process
    An example is the creation of the dag file. Not sure this is a bug but
    meanwhile, one must use this function to print information.

    This adds the // -- characters in front of the prin statements."""
    from easydev.console import purple
    print("// -- " + purple(mes))


class DOTParser(object):
    """Utility to manipulate the dot file returned by Snakemake

    This class is used in the *dag* and *rulegraph* rules used in the
    snakemake pipeline. The input must be a dag/rulegraph created by snakemake.

    Consider this example where the test file was created by snakemake --dag ::

        from sequana import sequana_data
        from sequana.snaketools import DOTParser

        filename = sequana_data("test_dag.dot")
        dot = DOTParser(filename)

        # creates test_dag.ann.dot locally
        dot.add_urls("test.dot", {"fastqc": "fastqc.html"})

    You can then convert the dag in an unix shell::

        dot -Tsvg test.ann.dot -o test.svg

    .. plot::

        from sequana import sequana_data
        from sequana.snaketools import DOTParser
        dot = DOTParser(sequana_data("test_dag.dot"))
        dot.add_urls("test.dot", {"fastqc": "fastqc.html"})
        from easydev import execute
        execute("dot -Tpng test.ann.dot -o test.png")
        from pylab import imshow, imread, xticks, yticks
        imshow(imread("test.png")); xticks([]) ;yticks([])

    """

    _name_to_drops = {'dag', 'conda', 'rulegraph', 'copy_multiple_files'}

    def __init__(self, filename, mode="v2"):
        """.. rubric:: constructor

         :param str filename: a DAG in dot format created by snakemake

        """
        self.filename = filename
        self.re_index = re.compile('(\d+)\[')
        self.re_name = re.compile('label = "(\w+)"')
        self.re_arrow = re.compile('(\d+) -> (\d+)')
        self.mode = mode

    def add_urls(self, output_filename=None, mapper={}, title=None):
        """Change the dot file adding URL on some nodes

        :param str output_filename: the DAG file in dot format (graphviz)
        :param dict mapper: a dictionary where keys are named after the rule
            names for which an HTML will be available (provided here as keys)

        """
        if self.mode == "v2":
            self._add_urls_mode2(output_filename, mapper, title)
        else:
            self._add_urls_mode1(output_filename, mapper, title)

    def _drop_arrow(self, index, indices_to_drop, title=None):
        for i in index:
            if i in indices_to_drop:
                return True
        return False

    def _add_urls_mode2(self, output_filename=None, mapper={}, title=None):
        # Open the original file
        with open(self.filename, "r") as fh:
            data = fh.read()

        if output_filename is None:
            import os
            output_filename = os.path.basename(self.filename)

        # The DOT parsing
        with open(output_filename.replace(".dot", ".ann.dot"), "w") as fout:
            indices_to_drop = set()
            for line in data.split("\n"):
                if line.strip().startswith("node["):
                    fout.write(' node[style="filled"; shape=box, ' +
                        ' color="black", fillcolor="#FCF3CF", ' +
                        ' fontname=sans, fontsize=10, penwidth=2];\n')
                    continue
                if line.strip().startswith("edge["):
                    fout.write(' edge[penwidth=2, color=black]; \n')
                    continue

                if line.strip() == "}":
                    if title:
                        fout.write('overlap=false\nlabel="%s"\nfontsize=10;\n}\n' % title)
                    else:
                        fout.write(line)
                    continue


                name = self.re_name.search(line)
                if name:
                    name = name.group(1)
                    if name in self._name_to_drops:
                        index = self.re_index.search(line).group(1)
                        indices_to_drop.add(index)
                    elif name in mapper.keys():
                        url = mapper[name]
                        newline = line.split(name)[0] + name +'"' 
                        newline += (' URL="%s", target="_parent", fillcolor="#5499C7"'
                                   '];\n') % url
                        #newline = line.replace('];', newline)
                        newline = newline.replace("dashed", "")
                        fout.write(newline)
                    else:
                        newline = line.split(name)[0] + name +'"];\n'
                        fout.write(newline)
                else:
                    arrow = self.re_arrow.findall(line)
                    if arrow:
                        index = arrow[0]
                        if not self._drop_arrow(index, indices_to_drop):
                            fout.write(line + "\n")
                    else:
                        line = line.replace("dashed", "")
                        fout.write(line + "\n")

    def _add_urls_mode1(self, output_filename=None, mapper={}, title=None):

        # Open the original file
        with open(self.filename, "r") as fh:
            data = fh.read()

        if output_filename is None:
            import os
            output_filename = os.path.basename(self.filename)

        # The DOT parsing
        with open(output_filename.replace(".dot", ".ann.dot"), "w") as fout:
            indices_to_drop = set()
            for line in data.split("\n"):
                name = self.re_name.search(line)
                if name:
                    name = name.group(1)
                    if name in self._name_to_drops:
                        index = self.re_index.search(line).group(1)
                        indices_to_drop.add(index)
                    elif name in mapper.keys():
                        url = mapper[name]
                        newline = (' URL="%s", target="_parent", color="blue"'
                                   '];\n') % url
                        newline = line.replace('];', newline)
                        newline = newline.replace("dashed", "")
                        fout.write(newline)
                    # else, we color in orange
                    else:
                        newline = line.replace('];', ',color="orange"];\n')
                        fout.write(newline)
                else:
                    arrow = self.re_arrow.findall(line)
                    if arrow:
                        index = arrow[0]
                        if not self.drop_arrow(index, indices_to_drop):
                            fout.write(line + "\n")
                    else:
                        line = line.replace("dashed", "")
                        fout.write(line + "\n")


class FileFactory(object):
    """Factory to handle a set of files

    ::

        from sequana.snaketools import FileFactory
        ff = FileFactory("H*.gz")
        ff.filenames

    A set of useful methods are available based on this convention::

        >>> fullpath = /home/user/test/A.fastq.gz
        >>> dirname(fullpath)
        '/home/user/test'
        >>> basename(fullpath)
        'A.fastq.gz'
        >>> realpath(fullpath) # is .., expanded to /home/user/test

        >>> all_extensions
        "fastq.gz"
        >>> extensions
        ".gz"

    """
    def __init__(self, pattern):
        """.. rubric:: Constructor

        :param pattern: can be a filename, list of filenames, or a global
            pattern (a unix regular expression with wildcards). For instance,
            "*/*fastq.gz"

        .. warning:: Only in Python 3.X supports the recursive global pattern
            for now.

        """
        self.pattern = pattern
        # A filename
        if isinstance(pattern, str) and os.path.exists(pattern):
            # Found one existing file
            self._glob = [pattern]
        # A pattern
        elif isinstance(pattern, str):
            try:
                self._glob = glob.glob(pattern, recursive=True)
            except:
                print("Recursive glob does not work in Python 2.X. Do not use **")
                self._glob = glob.glob(pattern)

        # a list of files
        elif isinstance(pattern, list):
            for this in pattern:
                if os.path.exists(this) is False:
                    raise ValueError("This file % does not exist" % this)
            self._glob = pattern[:]

    def _get_realpath(self):
        return [os.path.realpath(filename) for filename in self._glob]
    realpaths = property(_get_realpath,
                         doc=("real path is the full path + the filename"
                              " the extension"))

    def _get_basenames(self):
        return [os.path.split(filename)[1] for filename in self._glob]
    basenames = property(_get_basenames,
                         doc="list of filenames and their extensions without the path")

    def _get_filenames(self):
        return [this.split(".")[0] for this in self.basenames]
    filenames = property(_get_filenames,
                         doc="list of filenames (no path, no extension)")

    def _pathnames(self):
        pathnames = [os.path.split(filename)[0] for filename in self._glob]
        return pathnames
    pathnames = property(_pathnames,
                         doc="the relative path for each file (list)")

    def _pathname(self):
        pathname = set(self.pathnames)
        if len(pathname) == 1:
            return list(pathname)[0] + os.sep
        else:
            raise ValueError("found more than one pathname")
    pathname = property(_pathname, doc="the common relative path")

    def _get_extensions(self):
        filenames = [os.path.splitext(filename)[1] for filename in self._glob]
        return filenames
    extensions = property(_get_extensions, doc="the last extension (list)")

    def _get_all_extensions(self):
        filenames = [this.split('.', 1)[1] if "." in this else ""
                     for this in self.basenames]
        return filenames
    all_extensions = property(_get_all_extensions,
                              doc="the extensions (list)")

    def __len__(self):
        return len(self.filenames)

    def __str__(self):
        return "Found %s file(s)" % len(self)


class FastQFactory(FileFactory):
    """FastQ Factory tool

    In NGS experiments, reads are stored in a so-called FastQ file. The file is
    named::

        PREFIX_R1_SUFFIX.fastq.gz

    where _R1_ tag is always to be found. This is a single-ended case. In
    paired case, a second file is to be found::

        PREFIX_R2_SUFFIX.fastq.gz

    The PREFIX indicates the sample name. The SUFFIX does not convey any
    information per se. The default read tag ("_R[12]_") handle this case.
    It can be changed if data have another read tags. (e.g. "[12].fastq.gz")

    Yet, in long reads experiments (for instance), naming convention is
    different and may nor be single/paired end convention.

    In a directory (recursively or not), there could be lots of samples. This
    class can be used to get all the sample prefix in the :attr:`tags`
    attribute.

    Given a tag, one can get the corresponding file(s)::

        ff = FastQFactory("*fastq.gz")
        ff.tags
        ff.get_file1(ff.tags[0])
        len(ff)

    """
    def __init__(self, pattern, extension=["fq.gz", "fastq.gz"],
                 read_tag="_R[12]_", verbose=False):
        """.. rubric:: Constructor

        :param str pattern: a global pattern (e.g., ``H*fastq.gz``)
        :param list extension: not used
        :param str read_tag: regex tag used to join paired end files. Some
            characters need to be escaped with a '\' to be interpreted as
            character. (e.g. '_R[12]_\.fastq\.gz')
        :param bool verbose:
        """
        super(FastQFactory, self).__init__(pattern)

        # Filter out reads that do not have the read_tag
        # https://github.com/sequana/sequana/issues/480
        self._glob = [filename for filename in self._glob 
                      if re.search(read_tag, os.path.basename(filename))]

        if len(self.filenames) == 0:
            msg = "No files found with the requested pattern (%s)" % pattern
            logger.critical(msg)
            raise ValueError(msg)

        # Check the extension of each file (fastq.gz by default) TODO
        #for this in self.all_extensions:
        #    assert this.endswith(extension), \
        #        "Expecting file with %s extension. Found %s" % (extension, this)
        # identify a possible tag

        # check if tag is informative
        if "[12]" not in read_tag:
            msg = "Tag parameter must contain '[12]' for read 1 and 2."
            logger.error(msg)
            raise ValueError(msg)
        if read_tag == "[12]":
            msg = "Tag parameter must be more informative than just have [12]"
            logger.error(msg)
            raise ValueError(msg)

        # get name before the read tag (R[12])
        self.read_tag = read_tag
        re_read_tag = re.compile(read_tag)
        self.tags = list({re_read_tag.split(f)[0] for f in self.basenames})
        self.short_tags = [x.split("_")[0] for x in self.tags]
        if len(self.tags) == 0:
            msg = "No sample found. Tag '{0}' is not relevant".format(read_tag)
            logger.error(msg)
            raise ValueError(msg)

        if verbose:
            logger.info("Found %s projects/samples " % len(self.tags))

    def _get_file(self, tag, r):
        if tag is None:
            if len(self.tags) == 1:
                tag = self.tags[0]
            elif len(self.tags) > 1:
                raise ValueError("Ambiguous tag. You must provide one "
                                 "(sequana.FastQFactory)")
        else:
            assert tag in self.tags, 'invalid tag'
        # retrieve file of tag
        read_tag = self.read_tag.replace("[12]", r)
        candidates = [realpath for basename, realpath in
                      zip(self.basenames, self.realpaths)
                      if read_tag in basename and basename.startswith(tag)]

        if len(candidates) == 0 and r == "2":
            # assuming there is no R2
            return None
        elif len(candidates) == 1:
            return candidates[0]
        elif len(candidates) == 0:
            msg = "Found no valid matches. "
            msg += "Files must have the tag %s" % read_tag
            logger.critical(msg)
            raise Exception
        else:
            logger.critical('Found too many candidates: %s ' % candidates)
            msg = 'Found too many candidates or identical names: %s '\
                % candidates
            msg += "Files must have the tag %s" % read_tag
            raise ValueError(msg)

    def get_file1(self, tag=None):
        return self._get_file(tag, "1")

    def get_file2(self, tag=None):
        return self._get_file(tag, "2")

    def __len__(self):
        return len(self.tags)


def init(filename, namespace):
    """Defines the global variable __snakefile__ inside snakefiles

    If not already defined, __snakefile__ is created to hold the name of the
    pipeline. We also define initialise these variables :

        * expected_output as an empty list
        * toclean as an empty  list

    Use e.g. in quality_control pipeline for bwa_mem_dynamic option
    """
    # Create global name for later
    if "__snakefile__" in namespace.keys():
        pass
    else:
        # This contains the full path of the snakefile
        namespace['__snakefile__'] = filename
        namespace['__pipeline_name__'] = \
            os.path.split(filename)[1].replace(".rules", "")
        namespace['expected_output'] = []
        namespace['toclean'] = []

    # check requirements
    Module(filename.replace(".rules", "")).check('error')


def create_cleanup(targetdir, exclude=['logs']):
    """A script to include in directory created by the different pipelines to
cleanup the directory"""
    filename = targetdir + os.sep + "sequana_cleanup.py"
    with open(filename, "w") as fout:
        fout.write("""
import glob, os, shutil, time
from easydev import shellcmd

exclude = {}
for this in glob.glob("*"):
    if os.path.isdir(this) and this not in exclude and this.startswith('report') is False:
        print('Deleting %s' % this)
        time.sleep(0.1)
        shellcmd("rm -rf %s" % this)
shellcmd("rm -f  snakejob.* slurm-*")
shellcmd("rm -rf .snakemake")
shellcmd("rm -f sequana_cleanup.py")
""".format(exclude))
    return filename


def build_dynamic_rule(code, directory):
    """Create a rule in a unique file in .snakameke/sequana

    The filenames must be unique, and stored in .snakemake to not
    pollute /tmp

    """
    import os, uuid
    # Create directory if it does not exist
    from easydev import mkdirs
    mkdirs(directory + ".snakemake/sequana")
    # a unique identifier
    filename = directory
    filename += os.sep.join([".snakemake", "sequana", str(uuid.uuid4())])
    filename += ".rules"
    # Create the file and return its name so that it can be used inside a
    # pipeline
    fh = open(filename, "w")
    fh.write(code)
    fh.close()
    return filename


def add_stats_summary_json(json_list, parser):
    if not parser.stats:
        return
    for jfile in json_list:
        with open(jfile, 'r') as fp:
            jdict = json.load(fp)
        jdict['stats'] = parser.stats
        j = json.dumps(jdict)
        with open(jfile, 'w') as fp:
            print(j, file=fp)


class OnSuccess(object):
    def __init__(self, toclean=["fastq_sampling", "logs", "common_logs",
            "images", "rulegraph"]):
        self.makefile_filename = "Makefile"
        self.cleanup_filename = "sequana_cleanup.py"
        self.toclean = toclean

    def __call__(self):
        self.add_makefile()
        self.create_recursive_cleanup(self.toclean)

    def add_makefile(self):
        with open(self.makefile_filename, "w") as fh:
            fh.write("bundle:\n")
            if easydev.cmd_exists("pigz"):
                fh.write("\ttar cvf - * | pigz  -p 4 > results.tar.gz\n")
            else:
                fh.write("\ttar cvfz results.tar.gz *\n")
            fh.write("clean:\n")

            th = self.cleanup_filename
            fh.write('\tif [ -f %s ]; then python %s ; else echo "cleaned already"; fi;\n' % (th, th))

    def create_recursive_cleanup(self, additional_dir=[".snakemake"]):
        """Create general cleanup

        :param additional_dir: extra directories to remove

        """
        with open(self.cleanup_filename, "w") as fh:
            fh.write("""
import subprocess, glob, os
from easydev import shellcmd

for this in glob.glob("*"):
    if os.path.isdir(this):
        print(" --- Cleaning up %s directory" % this)
        if os.path.exists(this + os.sep + "sequana_cleanup.py"):
            pid = subprocess.Popen(["python", "sequana_cleanup.py"], cwd=this)
            pid.wait()  # we do not want to run e.g. 48 cleanup at the same time

# Remove some files
for this in ["README", "requirements.txt", 'runme.sh', 'config.yaml', 'stats.txt',
             "dag.svg", "rulegraph.svg", "*rules", "*.fa"]:
    try:
        shellcmd("rm %s" % this)
    except:
        print("%s not found (not deleted)" % this)

# Remove some directories
for this in {1}:
    try:
        shellcmd("rm -rf %s" % this)
    except:
        print("%s not found (not deleted)" % this)

shellcmd("rm -rf tmp/")
shellcmd("rm -f {0}")
print("done")
    """.format(self.cleanup_filename, additional_dir))


def get_pipeline_statistics():
    """Get basic statistics about the pipelines

    Count rule used per pipeline and returns a dataframe with rules as index 
    and pipeline names as columns

    ::

        from sequana.snaketools import get_pipeline_statistics
        df = get_pipeline_statistics()
        df.sum(axis=1).sort_values(ascending=False)
        df.sum(axis=0).plot(kind="barh")

    """
    pipelines = [m for m in modules if Module(m).is_pipeline()]
    rules = [rule for rule in modules if  Module(rule).is_pipeline() is False]

    import pandas as pd
    import numpy as np

    L, C = len(rules), len(pipelines)
    df = pd.DataFrame(np.zeros((L,C)), dtype=int, index=rules, columns=pipelines)

    for pipeline in pipelines:
        filename = Module(pipeline).path + "/%s.rules" % pipeline
        with open(filename) as fh:
            data =  fh.readlines()
            data = [x for x in data if x.strip().startswith("include:")]
            for line in data:
                for rule in rules:
                    if '"'+rule+'"' in line or "'"+rule+"'" in line or rule+"(" in line:
                        df.loc[rule, pipeline] += 1
    return df
