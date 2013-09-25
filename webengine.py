import shutil
import argparse
import os
import requests
from urlparse import urlparse
from sys import argv, exit

def worldEngine(url, resp):
    baseURL =  "http://" + urlparse(url).hostname 
    urlFile = "urlList"
    raw_files = "raw_files"
    converted_files = "converted_files"
    image_files = "image_files"

    from urlgatherer import get_urlList
    if get_urlList(args.url, urlFile, resp):
        print "!! Error: urlgatherer did not finish !!"
    else:
        print "** urlgatherer finished **"

    from filegatherer import get_filesFromList 
    if get_filesFromList(urlFile):
        print "!! Error: filegatherer did not finish !!"
    else:
        print "** filegatherer finished **"

    from fileconverter import get_convertedFiles
    if get_convertedFiles(raw_files, converted_files):
        print "!! Error fileconverter did not finish !!"
    else:
        print "** fileconverter finished **"

    from imagegatherer import get_imageFiles
    if get_imageFiles(raw_files, image_files, baseURL):
        print "!! Error imagegatherer did not finish !!"
    else:
        print "** imagegatherer finished **"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get all links on a page and save to a file")
    parser.add_argument("url", help="URL which to pull all the links out of")

    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "!! Sorry, error occurred. !!"
        exit()

    if worldEngine(args.url, resp):
        print "!! Error worldengine did not finish  !!"
    else:
        print "** site is habitable  **"
