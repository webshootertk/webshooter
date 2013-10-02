import shutil
import argparse
import os
import requests
from urlparse import urlparse
from sys import argv, exit

def worldEngine(url, href, src, option, resp):
    baseURL =  "http://" + urlparse(url).hostname 
    urlFile = "urlList"
    raw_files = "raw_files"
    html_files = "html_files"
    md_files = "md_files"
    image_files = "image_files"

    if option == "site":
        from urlgatherer import get_urlList
        if get_urlList(url, urlFile, resp):
            print "!! Error: urlgatherer did not finish !!"
        else:
            print "** urlgatherer finished **"

        from filegatherer import get_filesFromList 
        if get_filesFromList(urlFile, raw_files):
            print "!! Error: filegatherer did not finish !!"
        else:
            print "** filegatherer finished **"
    
    else:
        from sitegatherer import get_siteFiles
        if get_siteFiles(url, raw_files):
            print "!! Error: sitegaterer did not finish !!"
        else:
            print "** sitegaterer finished **"
   
    from filecorrector import get_correctedFiles 
    if get_correctedFiles(raw_files, html_files, href, src):
        print "!! Error: filecorrector did not finish !!"
    else:
        print "** filecorrector finished **"

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
    parser = argparse.ArgumentParser(description="get all content (html / images) from a wiki (site) and convert to markdown")
    parser.add_argument("url", help="URL to site or wiki")
    parser.add_argument("href", help="URL of the new site")
    parser.add_argument("src", help="Path to the image directory")
    parser.add_argument("option", default="site", help="add -w if a wiki Title Index page (the page that list all the pages in the wiki) if not a wiki leave blank")

    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "!! Sorry, site / wiki is not reachable, error occurred. !!"
        exit()

    if worldEngine(args.url, args.href, agrs.src, args.option, resp):
        print "!! Error worldengine did not finish  !!"
    else:
        print "** site is habitable  **"
        print " "
        print "new directory -> what is inside"
        print "raw_files   -> what came from the server (old html)"
        print "html_files  -> files from server with new href and src links (new html)"
        print "image_files -> all the image files from the old site (images)"
        print "md_files    -> the \"new html\" files converted to markdown (markdown)"
        print " "
        print "You may want to run md_files through filetrimmer.py to remove unwated headers and footers"
