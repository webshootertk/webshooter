#!/usr/local/bin/python

import shutil
import argparse
import os
import os.path
import requests
from urlparse import urlparse
from sys import argv, exit
from htmlcleaner import filtered_text
from bs4 import BeautifulSoup   

parser = argparse.ArgumentParser(description="Get all links on a page and save to a file")
parser.add_argument("url", help="URL which to pull all the links out of")
parser.add_argument("urlFile", help="Name of the file to save the list of urls in")


args = parser.parse_args()

resp = requests.get(args.url)
if resp.status_code >= 400:
	print "Sorry, error occurred."
	exit()

file_to_write = open(args.urlFile, "w")
file_to_write.write(resp.text)
file_to_write.close()

infile = open(args.urlFile).readlines()
clean_string = ''
for line in infile:
    clean_string += line
    
soup = BeautifulSoup(clean_string)
cleaner_string = ''

fullURL = "http://" + urlparse(args.url).hostname

for a in soup.find_all('a', href=True):
        
    if a['href'][0] != '#' and a['href'][:4] != "http" and a['href'].find("?") == -1 :
        nextURL = fullURL + a['href']
        cleaner_string += "%s\n" % nextURL
        outfile = open("urlList", "w")
        outfile.write(cleaner_string)
        outfile.close()

