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

    _wget =    "/usr/local/Cellar/wget/1.14/bin/wget"
    _r =       "-r"
    _wait =    "--wait=7"
    _random =  "--random-wait"
    _no =      "--no-check-certificate"
    _html =    "--accept=html"
    _convert = "--convert-links"
    _mirror =  "--mirror"
    _trust =   "--trust-server-names"
    _adjust =  "--adjust-extension"
    _user =    "--user="
    _passwd =  "--password="
   
    try:
        subprocess.call([_wget, _r, _wait, _random, _no, _convert, _mirror, _trust, _adjust, url]) 
        
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

