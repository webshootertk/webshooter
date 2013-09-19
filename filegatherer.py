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

file_to_read = open(args.urlFile)
infile_contents = file_to_read.read()
file_to_read.close()

for line in infile_contents:
    resp = requests.get(line)

    if resp.status_code >= 400:
        print "Sorry, error occurred getting %s. Moving on" % line
        break
    
    titleList = line.split("/")
    title = titleList[len(titleList -1)]
    
    file_to_write = open(title, "w")
    file_to_write.write(resp.text)
    file_to_write.close()
    
    time.sleep(3)
