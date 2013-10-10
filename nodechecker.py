#!/usr/local/bin/python

import requests
import shutil
import argparse
import os
import os.path
from sys import argv, exit

#path = "/Users/harris112/Projects/ESGF/esgf.github.io.wiki/Shutdown-Status.md"
path = "urlList"
node = "Node "
faq = "question "
rows = []
urls = []
newfile = []
end_file_flag = False
##  cd /Users/harris112/Projects/ESGF/esgf.github.io.wiki
##  git pull

infile = open(path).readlines()
clean_string = ''
for line in infile:
    line = line.strip()
    if end_file_flag:
        newfile.append(line)
    else:
        if "|" in line and "---" not in line:
            rows = line.split("|")
            if rows[0] == faq:
                newfile.append(line)
                end_file_flag = True
                continue 
            elif rows[0] == node: 
                newfile.append(line) 
                continue
            else:
                md = rows[1]
                urls = md.split("][")
                url = urls[0]
                url = url[2:]
                if not url: rows[3] = " down"
                else:
                    try:
                        resp = requests.get(url)
                        if resp.status_code >= 400: rows[3] = " down"
                        else: rows[3] = " up"
                    except: rows[3] = " down"
            
                temp =  "|".join(rows)
                newfile.append(temp)
        else: newfile.append(line)

outfile = open("test", "w")
#outfile = open(path, "w")
outfile.write("\n".join(newfile))
outfile.close()

## git commit -am "BOT: AUTO UPDATE NODE STATUS"
## git pull
## git push

print "done"
