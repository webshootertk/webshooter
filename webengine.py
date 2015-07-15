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
    whole_site = "whole_site"
    extracted_files = "extracted_files"
    html_files = "html_files"
    html_dirty_files = "html_dirty_files"
    completed_files = "completed_files"
    image_files = "image_files"
    
    file_ext = "md"
    if case == "hyde":
        file_ext = "html"
    print "Will save completed_files with the file extension % s" % file_ext

    if option != "site":
        from url_gatherer import get_urlList
        if get_urlList(url, urlFile, resp):
            print "!! Error: url_gatherer did not finish !!"
        else:
            print "** url_gatherer finished **"

        from file_gatherer import get_filesFromList 
        if get_filesFromList(urlFile, whole_site):
            print "!! Error: file_gatherer did not finish !!"
        else:
            print "** file_gatherer finished **"

    else:
        from site_gatherer import get_siteFiles
        if get_siteFiles(url, whole_site, "na", "na"):
            print "!! Error: site_gaterer did not finish !!"
        else:
            print "** site_gaterer finished **"

    from file_extractor import get_fileContent 
    if get_fileContent(whole_site, extracted_files):
        print "!! Error: file_corrector did not finish !!"
    else:
        print "** file_extractor finished **"

    from file_corrector import get_correctedFiles 
    if get_correctedFiles(extracted_files, html_files, href, src):
        print "!! Error: file_corrector did not finish !!"
    else:
        print "** file_corrector finished **"

    from html_table_2_markdown import get_correctedFiles
    if get_correctedFiles(html_files, html_dirty_files):
        print "!! Error: html_table_2_markdown did not finish !!"
    else:
        print "** html_table_2_markdown finished **"

    from file_converter import get_convertedFiles
    if get_convertedFiles(html_dirty_files, completed_files, file_ext):
        print "!! Error file_converter did not finish !!"
    else:
        print "** file_converter finished **"

    from image_gatherer import get_imageFiles
    if get_imageFiles(extracted_files, image_files, baseURL):
        print "!! Error image_gatherer did not finish !!"
    else:
        print "** image_gatherer finished **"
    
    from bold_cleanup import get_correctedFiles
    if get_correctedFiles(completed_files):
        print "!! Error bold_cleanup did not finish !!"
    else:
        print "** bold_cleanup finished **"

    from head_adder import add_headers
    if add_headers(completed_files, case):
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
        print "whole_site        -> The whole site from wget"
        print "extracted_files   -> just the body of the raw html files"
        print "html_files        -> extracted file corrected with new href and src links"
        print "html_dirty_files  -> html files with converted tables html to markdown"
        print "completed_files   -> md or html files as you asked for"
        print "image_files       -> all the image files from the old site (images)"
        print " "
        print "You may want to run md_files through file_trimmer.py to remove unwated headers and footers"
        print "If so remember to then run head_adder.py again by hand"
        print "to remove all generated files run webengine_cleanup.py"
