#!/usr/local/bin/python

import os.path
import requests
import time
import urlparse
from bs4 import BeautifulSoup
from random import randint
import sys
def get_siteFiles(url, save):
    print "this function is slow on purpose"
    
    if not os.path.exists(save):
        os.makedirs(save)

    try:
       temp = 0

    except: 
        print sys.exc_info()[0]


if __name__ == "__main__":
    import shutil
    import argparse
    import os
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Get all the pages of a website")
    parser.add_argument("url", help="url of site to get (wget -R )")
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
