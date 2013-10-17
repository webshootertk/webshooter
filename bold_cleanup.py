#!/usr/local/bin/python
import shutil
import os
import os.path
def get_correctedFiles(path):

    for f in os.listdir(path):
        print "correcting file %s" % f
        infile = open(os.path.join(path, f)).read()
        infile = infile.replace("**","")
        outfile = open(os.path.join(path, f), "w")
        outfile.write(infile)
        outfile.close()

if __name__ == "__main__":
    import shutil
    import argparse
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="converts all the href and scr to point to full path / different location")
    parser.add_argument("path", help="folder containing html (raw) files")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_correctedFiles(args.path):
        print "Error"
    else:
        print "Done"






