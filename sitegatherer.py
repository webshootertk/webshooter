#!/usr/local/bin/python

import os.path
import requests
import time
import urlparse
import sys
import subprocess
import select
import urlparse
from bs4 import BeautifulSoup
from random import randint
def get_siteFiles(url, save):
    print "this function is slow on purpose"
    print " "

    if not os.path.exists(save):
        os.makedirs(save)

    try:
        subprocess.call(["wget", "-r", "--accept=html", "--wait=5", "--random-wait", url])
        
        folder = urlparse.urlparse(url)
        folder = folder.netloc
        os.rename(folder, save)
    
    except: 
        print sys.exc_info()[0]


if __name__ == "__main__":
    import shutil
    import argparse
    import os
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Get all the pages of a website (wget -r)")
    parser.add_argument("url", help="url of site to get")
    parser.add_argument("save", help="folder name to save raw htlm files in")

    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "Sorry, site not reachable, error occurred."
        exit()

    if get_siteFiles(args.url, args.save):
        print "Error"
    else:
        print "Done"
