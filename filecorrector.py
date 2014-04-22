#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup   
import html2text
from htmlcleaner import filtered_text
import os
import os.path
import shutil
from sys import argv, exit
import urlparse

def get_correctedFiles(path, save, url, img):

    if not os.path.exists(save):
        os.makedirs(save)

    for f in os.listdir(path):
        print "correcting file %s" % f
        infile = open(os.path.join(path, f)).read()
        
        soup = BeautifulSoup(infile, "html5lib")
        for tag in soup.find_all(lambda t: 'href' in t.attrs or 'src' in t.attrs):
            if 'href' in tag.attrs:
                url_parts = urlparse.urlsplit(tag.attrs["href"])
                full_path = tag.attrs["href"]
                hrefpath = url_parts.path
                if full_path[0:4] != "http" or full_path[0:5] != " http":
                    # for wiki conversion (moin moin wikis)
                    # hrefpath = hrefpath.replace("/", "|")
                    if hrefpath[0:6] == "|wiki|":
                        hrefpath = hrefpath[6:]
                    tag.attrs["href"] = urlparse.urljoin(url, hrefpath)
            else:
                url_parts = urlparse.urlsplit(tag.attrs["src"])
                srcpath = url_parts.path
                srcparts = srcpath.split("/")
                srcpath = srcparts[len(srcparts) -1]
                tag.attrs["src"] = urlparse.urljoin(img, srcpath)

        
        outfile = open(os.path.join(save, f), "w")
        outfile.write(soup.encode("ascii", "xmlcharrefreplace"))
        outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="converts all the href and scr to point to full path / different location")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("save", help="folder to put converted html files")
    parser.add_argument("url", help="What is the full path / new url for page links")
    parser.add_argument("img", help="What is the full path / new url for images")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_correctedFiles(args.path, args.save, args.url, args.img):
        print "Error"
    else:
        print "Done"
