#!/usr/local/bin/python

import argparse
import os
import os.path
import shutil
from bs4 import BeautifulSoup
from sys import argv, exit

def save_files(path, filename, content):
    outfile = open(os.path.join(path, filename), "w")
    outfile.write(content.encode("ascii", "xmlcharrefreplace"))
    outfile.close()
    print "saved file % s" % os.path.join(path, filename)

def get_file(root, save, f, path, outfile):
    infile = open(os.path.join(root, f)).read()
    tree = BeautifulSoup(infile, "html5lib")

    #this is bad and I feel bad
    try:
        content = tree.body.find("div", id="content").prettify()
        #print "found <div id=\"content\">"
    except:
        try:
            content = tree.body.find("div", id="container").prettify()
            #print "found <div id=\"container\">"
        except:
            try:
                content = tree.body.prettify()
                #print "found <body>"
            except:
                content = infile
                #print "Leaving file as is"
    #end of feeling bad

    filename = outfile
    if filename in ("index.html", "index.php"):
        filename = path[len(path) - 1] + ".html"
    save_files(save, filename, content)    

def get_fileContent(path, save):

    if not os.path.exists(save):
        os.makedirs(save)

    pdf = "pdf_files"
    images = "image_files"
    docs = "doc_files"

    if not os.path.exists(pdf):
        os.makedirs(pdf)
    if not os.path.exists(images):
        os.makedirs(images)
    if not os.path.exists(docs):
        os.makedirs(docs)


    for root, dirs, files in os.walk(path):
        path = root.split('/')
        for f in files:
            extension = os.path.splitext(f)[1]
            if extension == ".pdf":
                save_files(pdf, f, f)

            if extension in (".PNG", ".png", ".jpeg", ".JPEG", ".jpg", ".JPG", ".gif", ".GIF"):
                save_files(images, f, f)

            if extension in (".xml", ".doc", ".docx", ".ppt", ".pptx", ".txt"):
                save_files(docs, f, f)

            if extension in (".html", ".php"):
                get_file(root, save, f, path, f)

            elif ".php?" in extension:
                parts = f.split("?")
                newfile = parts[1] + "-" + parts[0]
                get_file(root, save, f, path, newfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gets the body of all html and php files")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("save", help="folder to save no table html (edited) files")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_fileContent(args.path, args.save):
        print "Error"
    else:
        print "Done"
