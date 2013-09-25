def worldEngine(url, resp):
    urlFile = "urlList"
    raw_files = "raw_files"
    converted_files = "converted_files"

    from urlgatherer import get_urlList
    if get_urlList(args.url, urlFile, resp):
        print "Error: urlgatherer did not finish"
    else:
        print "urlgatherer finished"

    from filegatherer import get_filesFromList 
    if get_filesFromList(urlFile):
        print "Error: filegatherer did not finish"
    else:
        print "filegatherer finished"

    from fileconverter import get_convertedFiles
    if get_convertedFiles(raw_files, converted_files):
        print "Error fileconverter did not finish"
    else:
        print "fileconverter finished"

if __name__ == "__main__":
    import shutil
    import argparse
    import os
    import requests
    from sys import argv, exit

    parser = argparse.ArgumentParser(description="Get all links on a page and save to a file")
    parser.add_argument("url", help="URL which to pull all the links out of")

    args = parser.parse_args()

    resp = requests.get(args.url)
    if resp.status_code >= 400:
        print "Sorry, error occurred."
        exit()

    if worldEngine(args.url, resp):
        print "Error worldengine did not finish"
    else:
        print "site is habitable"
