#!/usr/local/bin/python

import argparse
import os
import requests
import shutil
from sys import argv, exit
from urlparse import urlparse

def worldEngine(url, href, src, option, resp, case):
    baseURL =  "http://" + urlparse(url).hostname 
    urlFile = "urlList"
    raw_files = "raw_files"
    html_files = "html_files"
    md_files = "md_files"
    image_files = "image_files"

    if option != "site":
        from url_gatherer import get_urlList
        if get_urlList(url, urlFile, resp):
            print "!! Error: url_gatherer did not finish !!"
        else:
            print "** url_gatherer finished **"

        from file_gatherer import get_filesFromList 
        if get_filesFromList(urlFile, raw_files):
            print "!! Error: file_gatherer did not finish !!"
        else:
            print "** file_gatherer finished **"
    
    else:
        from site_gatherer import get_siteFiles
        if get_siteFiles(url, raw_files, "na", "na"):
            print "!! Error: site_gaterer did not finish !!"
        else:
            print "** site_gaterer finished **"
   
    from file_corrector import get_correctedFiles 
    if get_correctedFiles(raw_files, html_files, href, src):
        print "!! Error: file_corrector did not finish !!"
    else:
        print "** file_corrector finished **"

    from file_converter import get_convertedFiles
    if get_convertedFiles(html_files, md_files):
        print "!! Error file_converter did not finish !!"
    else:
        print "** file_converter finished **"

    from image_gatherer import get_imageFiles
    if get_imageFiles(raw_files, image_files, baseURL):
        print "!! Error image_gatherer did not finish !!"
    else:
        print "** image_gatherer finished **"
    
    from bold_cleanup import get_correctedFiles
    if get_correctedFiles(md_files):
        print "!! Error bold_cleanup did not finish !!"
    else:
        print "** bold_cleanup finished **"

    from head_adder import add_headers
    if add_headers(md_files, case):
        print "!! Error head_adder did not finish !!"
    else:
        print "** head_adder finished **"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get all content (html / images) from a wiki (site) and convert to markdown")
    parser.add_argument("url", help="URL to site or wiki")
    parser.add_argument("href", help="URL of the new site")
    parser.add_argument("src", help="Path to the image directory")
    parser.add_argument("type", help="\"site\" for full website or \"wiki\" for wiki Title Index page")
    parser.add_argument("case", help="jekyll, hyde, none")

    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "!! Sorry, site / wiki is not reachable, error occurred. !!"
        exit()

    if worldEngine(args.url, args.href, args.src, args.type, resp, args.case):
        print "!! Error worldengine did not finish  !!"
    else:
        print "** site is habitable  **"
        print " "
        print "raw_files   -> what came from the server (old html)"
        print "html_files  -> files from server with new href and src links (new html)"
        print "md_files    -> the \"new html\" files converted to markdown (markdown)"
        print "image_files -> all the image files from the old site (images)"
        print " "
        print "You may want to run md_files through file_trimmer.py to remove unwated headers and footers"
        print "If so remember to then run head_adder.py again by hand"
