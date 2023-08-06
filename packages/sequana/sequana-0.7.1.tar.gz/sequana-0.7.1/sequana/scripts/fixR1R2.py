import os, glob




def fix_identifier(zipped_filenames, directory):

    N = len(zipped_filenames)

    for i, filename in enumerate(zipped_filenames):
        print("--------------- {}/{} ".format(i+1, N))
        # unzip file
        print('decompressing {}'.format(filename))
        cmd = "unpigz {}".format(filename)
        retcode = os.system(cmd)
        assert retcode == 0

        print("Fixing {}".format(filename))
        filename2 = filename.replace(".gz", "")

        # Fix it
        with open(filename2, "r") as fin:
            with open("fix/{}".format(filename2), "w") as fout:
                if "R1" in filename:
                    suffix = "/1"
                elif "R2" in filename:
                    suffix = "/2"
                else:
                    raise ValueError("Expecting R1 or R2 in the filename")

                for line in fin.readlines():
                    if line.startswith("@"):
                        line = line.strip() + "{}\n".format(suffix)
                    fout.write(line)

        print('compressing {}'.format(filename))
        cmd = "pigz {}".format(filename2)
        retcode = os.system(cmd)
        assert retcode == 0

if __name__ == "__main__":

    import sys
    if len(sys.argv) != 2:
        print( "usage: python fixR1R2.py fix" + "\nwhere fix is the directory where fixed files are copied")
        sys.exit()

    directory = sys.argv[1]

    try:os.mkdir(directory)
    except:pass

    zipped_filenames = glob.glob("test*.fastq.gz")

    fix_identifier(zipped_filenames, directory)
