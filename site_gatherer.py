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


def get_siteFiles(url, save, user, passwd):
    print " ---------------------------------- "
    print "| this function is slow on purpose |"
    print " ---------------------------------- "

    fold = urlsplit(url)
    folder = fold.hostname
    location = save

    _wget =    "wget"
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
        if user == "na":
            subprocess.call([_wget, _r, _wait, _random, _no, url])
        elif user == "html":
            subprocess.call([_wget, _r, _wait, _random, _no, _html , url])
        else:
            subprocess.call([_wget, _r, _wait, _random, _no, _user+user, _passwd+passwd, url])
        
        os.rename(folder, location)
    
    except: 
        print "except"
        print sys.exc_info()[0]

##### MOVED TO file_extractor ######
#    if not os.path.exists(save):
#        os.makedirs(save)
#
#    for dirpath, dirnames, filenames in os.walk(os.path.abspath(location)):
#        for filename in filenames:
#            root, ext = os.path.splitext(filename)
#            if ext in (".php", ".html", ""):
#                print filename
#                shutil.copyfile(os.path.join(dirpath, filename), os.path.join(save, root + ".html"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="wget -r --wait=7 --random-wait --no-check-certificate --user=X --passwd=Y URL")
    parser.add_argument("url", help="url of site")
    parser.add_argument("user", help="username if required if not enter \"na\"")
    parser.add_argument("passwd", help="password if required if not enter \"na\"")
    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "Sorry, site not reachable, error occurred."
        exit()

    save = "raw_files"
    if get_siteFiles(args.url, save, args.user, args.passwd):
        print "Error"
    else:
        print "Done"
