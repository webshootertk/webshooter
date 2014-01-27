#!/usr/local/bin/python
import argparse
from bs4 import BeautifulSoup
import os
import os.path
from random import randint
import requests
import select
import shutil
import subprocess
import sys
from sys import argv, exit
import time
import urlparse
from urlparse import urlparse
from urlparse import urlsplit


def get_siteFiles(url):
    print " ---------------------------------- "
    print "| this function is slow on purpose |"
    print " ---------------------------------- "

    if not os.path.exists(save):
        os.makedirs(save)

    fold = urlsplit(url)
    folder = fold.hostname
    location = "whole_site"

    wget =    "wget"
    r =       "-r"
    wait =    "--wait=7"
    random =  "--random-wait"
    no =      "--no-check-certificate"
    convert = "--convert-links"
    mirror =  "--mirror"
    trust =   "--trust-server-names"
    adjust =  "--adjust-extension"
    user =    "--user="
    passwd =  "--password="
   
    try:
        subprocess.call([wget, r, wait, random, no, convert, mirror, trust, adjust, url]) 
        
        os.rename(folder, location)
    
    except: 
        print sys.exc_info()[0]

    for dirpath, dirnames, filenames in os.walk(os.path.abspath(location)):
        for filename in filenames:
            root, ext = os.path.splitext(filename)
            if ext in (".php", ".html"):
                print filename
                shutil.copyfile(os.path.join(dirpath, filename), os.path.join(save, root + ".html"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="wget ALL the pages")
    parser.add_argument("url", help="url of site")
    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "Sorry, site not reachable, error occurred."
        exit()

    save = "raw_files"
    if get_siteFiles(args.url):
        print "Error"
    else:
        print "Done"

