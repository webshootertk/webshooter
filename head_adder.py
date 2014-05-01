#!/usr/local/bin/python

import argparse
import os
import os.path
import shutil
from sys import argv, exit

def add_headers(path, types):

    for f in os.listdir(path):
        print "correcting file %s" % f
        infile = open(os.path.join(path, f)).read()
        if case == "jekyll":
            infile = "---\n" + \
                     "layout: default\n" + \
                     "title:\n" + \
                     "---\n" + \
                     "\n" + \
                     infile
        
        elif case == "hyde":
            infile = "---\n" + \
                     "title: \n" + \
                     "subtitle: \n" + \
                     "description: \n" + \
                     "---\n" + \
                     "\n" + \
                     "{% extends \"topbar.j2\" %}\n" + \
                     "\n" + \
                     "{% block container %}" + \
                     infile + \
                     "\n{% endblock container %}"

        outfile = open(os.path.join(path, f), "w")
        outfile.write(infile)
        outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="addes jekyll or hyde headers to all the pages")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("case", help="hyde or jekyll")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if type not in ("jekyll","hyde"):
        stderr.write("type must be either \"jekyll\" or \"hyde\"")
        exit()

    if add_headers(args.path, args.case):
        print "Error"
    else:
        print "Done"
