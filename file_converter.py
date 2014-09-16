#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup   
import html2text
from html_cleaner import filtered_text
import os
import os.path
import shutil
from sys import argv, exit

def get_convertedFiles(path, save, ext):

    if not os.path.exists(save):
        os.makedirs(save)
    #need to pass in hyde flag
    #if hyde-flag is true
        #file_ext = ".html"
    #else
        #file_ext = ".md"
    file_ext = ".md"
    
    if ext is "html":
        file_ext = ".html"

    for f in os.listdir(path):
        extension = os.path.splitext(f)[1]
        fileName = os.path.abspath(path) + "/" + f
        if fileName[0] == "/":
            fileName = fileName[1:]
        fileName = fileName.replace("/","-")
        #print "filename is " + fileName
        if extension in (".php", ".html"):
            infile = open(os.path.join(path, f)).read()
            h2t = html2text.HTML2Text()
            content = h2t.handle(infile)
            if extension == ".html":
                fileName = fileName[0:len(fileName) -5] + file_ext
            elif extension == ".php":
                fileName = fileName[0:len(fileName) -4] + file_ext
            else:
                print "Failed"
                fileName = f + file_ext
            print fileName
            outfile = open(os.path.join(save, fileName), "w")
            outfile.write(content.encode("ascii", "xmlcharrefreplace"))
            outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="converts html (raw) files to markdown")
    parser.add_argument("path", help="folder containing a html (raw) files")
    parser.add_argument("save", help="folder to put markdown files")
    parser.add_argument("ext", help="html of md")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_convertedFiles(args.path, args.save, args.ext):
        print "Error"
    else:
        print "Done"
