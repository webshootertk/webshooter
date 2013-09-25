#!/usr/local/bin/python

import shutil
import os
import os.path
from htmlcleaner import filtered_text
from bs4 import BeautifulSoup   
import html2text

def get_convertedFiles(path, save):
    for f in os.listdir(path):
        extension = os.path.splitext(f)[1]
        if extension not in (".md", ".py", ".pyc"):
            print "converting file %s" % f
            infile = open(os.path.join(path, f)).read()
            h2t = html2text.HTML2Text()
            content = h2t.handle(infile)
            if extension == ".html":
                fileName = f[0:len(f) -5] + ".md"
            else:
                fileName = f + ".md"
            outfile = open(os.path.join(save, fileName), "w")
            outfile.write(content.encode("ascii", "xmlcharrefreplace"))
            outfile.close()

if __name__ == "__main__":
    import shutil
    import argparse
    import os
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Get all the pages from a file of links")
    parser.add_argument("path", help="folder containing a raw files")
    parser.add_argument("save", help="folder to put clean files")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if not os.path.exists(args.save):
        os.makedirs(args.save)

    if get_convertedFiles(args.path, args.save):
        print "Error"
    else:
        print "Done"




