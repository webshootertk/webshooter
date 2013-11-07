#!/usr/bin/python

import subprocess
import urllib
import shutil
import argparse
import os
import os.path
import traceback
import git
import time
from sys import argv, exit

repo = git.Repo( '/home/harris112/Projects/aims-site.wiki' )
repo.git.pull()

path_to_file = "Site-Status.md"
URL = "site "
down = " down "
up = " up "
date = " " + time.strftime("%x") + " : " + time.strftime("%X")

rows = []
urls = []
newfile = []

infile = open(path_to_file).readlines()
clean_string = ''
for line in infile:
    line = line.strip()
    if "|" in line and "---" not in line:
    	rows = line.split("|")
        if rows[0] == URL: 
            newfile.append(line) 
            continue
        else:
            url = rows[0].strip()
            try:
                print url
                resp = urllib.urlopen(url)
                code = resp.next()
                if resp.getcode() != 200: 
                    rows[1] = down
                else: 
                    rows[1] = up
            except: 
                rows[1] = down #print traceback.format_exc()

            temp =  "|".join(rows)
            newfile.append(temp)
    else: 
      if "---" in line:
        newfile.append(line)

newfile.append("last updated: " + date)

outfile = open(path_to_file, "w")
outfile.write("\n".join(newfile))
outfile.close()

status = repo.git.status()
if "nothing to commit" not in status:
  repo.git.commit(("-am", "MBH: hourly status update"))
  repo.git.push()
else: print status

print "done"
