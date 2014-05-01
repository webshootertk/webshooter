#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup   
from html_cleaner import filtered_text
import os
import os.path
import shutil
from sys import argv, exit

def get_cleanFiles(path, topfile, bottomfile):
    jekyll = "---\nlayout: default\ntitle: \n---\n\n"

    for f in os.listdir(path):
        print "trimming file %s" % path 

        infile = open(os.path.join(path, f)).readlines()
        infile = infile[topfile: len(infile) - bottomfile]
        
        save = "".join(infile)
        save = jekyll + save
        outfile = open(os.path.join(path, f), "w")
        outfile.write(save.encode("ascii", "xmlcharrefreplace"))
        outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="removes X lines from top and Y lines from bottom of a file")
    parser.add_argument("path", help="folder containing files")
    parser.add_argument("topfile", help="number of lines to remove from the top of the file (header, nav, menu)")
    parser.add_argument("bottomfile", help="number of lines to remove from the bottom of the file (footer, nav, links)")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_cleanFiles(args.path, int(args.topfile), int(args.bottomfile)):
        print "Error"
    else:
        print "Done"





