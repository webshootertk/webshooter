#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup   
from html_cleaner import filtered_text
import os
import os.path
import shutil
from sys import argv, exit

def get_cleanFiles(path, save, topfile, bottomfile):
    
    if not os.path.exists(args.save):
        os.makedirs(args.save)

    for root, _, files in os.walk(path):
        for f in files:
            extension = os.path.splitext(f)[1]
            if extension not in (".md", ".py", ".pyc"):
                print "cleaning file %s" % f
                infile = open(os.path.join(root, f)).readlines()
                infile = infile[topfile: len(infile) - bottomfile]
                cleaned = []
                for line in infile:
                    line = line.strip()
                    line = ">\n".join(line.split(">"))
                    
                    cleaned.append(line)
    
                clean_string = "\n".join(cleaned)
                cleaned_soup = BeautifulSoup(clean_string, "html5lib")
                clean_string = filtered_text(cleaned_soup.body, ["a", "img"])
                cleaner_string = ''
                for line in clean_string.split("\n"):
                    line = line.strip()
                    if len(line):
                        cleaner_string += "%s\n" % line

                if extension == ".html":
                    fileName = f[0:len(f) -5] + ".md"
                else:
                    fileName = f + ".md"

                outfile = open(os.path.join(path, "..", save, fileName), "w")
                outfile.write(cleaner_string.encode("ascii", "xmlcharrefreplace"))
                outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="strips out all html, and removes X, Y lines from the top and bottom of the file.")
    parser.add_argument("path", help="folder containing raw files")
    parser.add_argument("save", help="folder to put clean files")
    parser.add_argument("topfile", help="number of lines to remove from top of file")
    parser.add_argument("bottomfile", help="number of lines to remove from teh bottom of file")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_cleanFiles(args.path, args.save, int(args.topfile), int(args.bottomfile)):
        print "Error"
    else:
        print "Done"
