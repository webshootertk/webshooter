#!/usr/local/bin/python

import requests
import os.path
from urlparse import urlparse
from bs4 import BeautifulSoup   
def get_urlList(url, urlFile, resp):
    file_to_write = open(urlFile, "w")
    file_to_write.write(resp.text)
    file_to_write.close()

    infile = open(urlFile).readlines()
    clean_string = ''
    for line in infile:
        clean_string += line
    
    soup = BeautifulSoup(clean_string)
    cleaner_string = ''

    fullURL = "http://" + urlparse(url).hostname

    for a in soup.find_all('a', href=True):
        
        if a['href'][0] != '#' and a['href'][:4] != "http" and a['href'].find("?") == -1 :
            if a['href'][0] == "/":
                nextURL = fullURL + a['href']
            else:
                nextURL = fullURL + "/" + a['href']
            
            cleaner_string += "%s\n" % nextURL
            outfile = open(urlFile, "w")
            outfile.write(cleaner_string)
            outfile.close()

    print ("Created list of URLs in %s" % urlFile)
    return

if __name__ == "__main__":
    import shutil
    import argparse
    import os
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Get all links on a page and save to a file")
    parser.add_argument("url", help="URL which to pull all the links out of")
    parser.add_argument("urlFile", help="Name of the file to save the list of urls in")


    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "Sorry, error occurred."
        exit()

    if get_urlList(args.url, args.urlFile, resp):
        print "Error"
    else:
        print "Done"
