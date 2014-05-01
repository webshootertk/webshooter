#!/usr/local/bin/python

import argparse
import os
import os.path
import shutil
from sys import argv, exit

def get_correctedFiles(path):

    for f in os.listdir(path):
        print "removing bold and italic markup in file %s" % f
        infile = open(os.path.join(path, f)).read()
        infile = infile.replace("**","")
        infile = infile.replace(" _","")
        infile = infile.replace("_ ","")
        infile = infile.replace(" __ ","")
        outfile = open(os.path.join(path, f), "w")
        outfile.write(infile)
        outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="removes all bad bold and italic markup")
    parser.add_argument("path", help="folder containing html (raw) files")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_correctedFiles(args.path):
        print "Error"
    else:
        print "Done"
