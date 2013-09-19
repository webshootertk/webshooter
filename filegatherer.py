#!/usr/local/bin/python

import shutil
import argparse
import os
import os.path
import requests
import time
from sys import argv, exit
from htmlcleaner import filtered_text
from bs4 import BeautifulSoup   

parser = argparse.ArgumentParser(description="Get all the pages from a file of links")
parser.add_argument("urlFile", help="file containing a list of URLs")

args = parser.parse_args()

if not os.path.exists(args.urlFile):
    stderr.write("Input file %s not found." % args.urlFile)
    exit()

files = "temp_files"
if not os.path.exists(files):
    os.makedirs(files)

file_to_read = open(args.urlFile)
infile_contents = file_to_read.readlines()
file_to_read.close()

for line in infile_contents:
    try:
        line = line[:-1]
        resp = requests.get(line)
        if resp.status_code >= 400:
            print "Sorry, error occurred getting %s" % line
            print "Status Code: %s" % resp.status_code
            continue
    
        titleList = line.split("/")
        title = titleList[len(titleList) - 1] + ".html"
        text = resp.text 
        file_to_write = open(os.path.join(files, title), "w")
        file_to_write.write(text.encode("ascii", "xmlcharrefreplace"))
        file_to_write.close()
    except: 
        print "exception file: %s" % line
        print "exception status: %s" % resp.status_code

    time.sleep(1)
