#!/usr/local/bin/python

import os.path
import requests
import time
from bs4 import BeautifulSoup
from random import randint
import sys
def get_filesFromList(urlFile):
    print "this functino is slow on purpose"

    files = "raw_files"
    resp = ""

    if not os.path.exists(files):
        os.makedirs(files)

    file_to_read = open(urlFile)
    infile_contents = file_to_read.readlines()
    file_to_read.close()
    count = 0
    total = len(infile_contents)

    for line in infile_contents:
    
        time.sleep(randint(2,9))
        count += 1
        try:
            line = line[:-1]
            resp = requests.get(line)
            if resp.status_code >= 400:
                print "Sorry, error occurred getting %s" % line
                print "Status Code: %s" % resp.status_code
                continue
    
            titleList = line.split("/")
            title = titleList[len(titleList) - 1]
            text = resp.text
            print "Saving file %s (%d of %d)" % (title, count, total)
            file_to_write = open(os.path.join(files, title), "w")
            file_to_write.write(text.encode("ascii", "xmlcharrefreplace"))
            file_to_write.close()
        except: 
            print "exception file: %s" % line
            print "Status Code: %s" % resp.status_code
            print sys.exc_info()[0]


if __name__ == "__main__":
    import shutil
    import argparse
    import os
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Get all the pages from a file of links")
    parser.add_argument("urlFile", help="file containing a list of URLs")

    args = parser.parse_args()

    if not os.path.exists(args.urlFile):
        stderr.write("Input file %s not found." % args.urlFile)
        exit()

    if get_filesFromList(args.urlFile):
        print "Error"
    else:
        print "Done"
