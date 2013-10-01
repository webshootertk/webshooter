#!/usr/local/bin/python

import shutil
import os
import os.path
from htmlcleaner import filtered_text
from bs4 import BeautifulSoup   
import html2text

def get_correctedFiles(path, save, url, img):

    if not os.path.exists(save):
        os.makedirs(save)

    for f in os.listdir(path):
        print "correcting file %s" % f
        infile = open(os.path.join(path, f)).read()
        
        soup = BeautifulSoup(infile, "html5lib")
        for tag in soup.find_all(lambda t: 'href' in t.attrs or 'src' in t.attrs):
            if 'href' in t.attrs:
                url_parts = urlparse.urlsplit(tag.attrs["href"])
                path = url_parts.path
                if path[0:6] == "/wiki/":
                    path = path[6:] 
                    path = path.replace("/", "|")   
                    path = "/wiki/" + path + ".md"
                    tag.attrs["href"] = urlparse.urljoin(url, path)
            else:
                url_parts = urlparse.urlsplit(tag.attrs["src"])
                path = url_parts.path
                if path[0:6] == "/wiki/":
                    title = path.split("/")
                    title = title[len(title) - 1]
                    tag.attrs["src"] = urlparse.urljoin(img, title)

        
        outfile = open(os.path.join(save, f), "w")
        outfile.write(content.encode("ascii", "xmlcharrefreplace"))
        outfile.close()

if __name__ == "__main__":
    import shutil
    import argparse
    import os
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Converts all the href and scr to point to new locations")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("save", help="folder to put clean files")
    parser.add_argument("url", help="What is th new url? (url to replace path url's with)")
    parser.add_argument("img", help="Where will images be living? (src for img tags)")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_correctedFiles(args.path, args.save, args.url, args.img):
        print "Error"
    else:
        print "Done"





