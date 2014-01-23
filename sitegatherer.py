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


def get_siteFiles(url, save, user, passwd):
    print "--------------------------------"
    print "this function is slow on purpose"
    print "--------------------------------"

    if not os.path.exists(save):
        os.makedirs(save)

    try:
        subprocess.call(["wget", "-r", "--wait=7", "--random-wait", "--no-check-certificate", "--user="+user, "--password="+passwd, url])
        
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
