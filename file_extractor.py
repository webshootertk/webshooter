#!/usr/local/bin/python

import argparse
import os
import os.path
import shutil
from bs4 import BeautifulSoup
from sys import argv, exit

def get_fileContent(path, save):
    if not os.path.exists(save):
        os.makedirs(save)

    for f in os.listdir(path):
        print "extracting content from file %s" % f
        infile = open(os.path.join(path, f)).read()

        tree = BeautifulSoup(infile, "html5lib")

        try:
            content = tree.body.find("div", id="content").prettify()
            print "found <div id=\"content\">"
        except:
            try:
                content = tree.body.find("div", id="container").prettify()
                print "found <div id=\"container\">"
            except:
                try:
                    content = tree.body.prettify()
                    print "found <body>"
                except:
                    content = infile
                    print "Leaving file as is"

        outfile = open(os.path.join(save, f), "w")
        outfile.write(content.encode("ascii", "xmlcharrefreplace"))
        outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="removes all bad bold and italic markup")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("save", help="folder to save no table html (edited) files")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_fileContent(args.path, args.save):
        print "Error"
    else:
        print "Done"
