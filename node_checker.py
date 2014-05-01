#!/usr/bin/python

import argparse
import git
import os
import os.path
import shutil
import subprocess
from sys import argv, exit
import traceback
import time
import urllib

repo = git.Repo('/home/harris112/Projects/esgf.github.io.wiki')
repo.git.pull()

path_to_file = "Peer-Node-Status.md"
URL = " URL "
node_manager = "esgf-node-manager"
esgf_web_fe = "esgf-web-fe"
thredds = "thredds"
up = " up "
down = " down "
date = time.strftime("%x") + " : " + time.strftime("%X")
none = " - "
rows = []
urls = []
newfile = []
end_file_flag = False

infile = open(path_to_file).readlines()
clean_string = ''
for line in infile:
    line = line.strip()
    if "|" in line and "---" not in line:
    	rows = line.split("|")
        if rows[1] == URL: 
            newfile.append(line) 
            continue
        else:
            url = rows[1].strip()
            if not url: 
                rows[3] = none
            else:
                try:
                    print url
                    resp = urllib.urlopen(url)
                    code = resp.next()
                    if node_manager not in code and esgf_web_fe not in code and thredds not in code: 
                        rows[3] = down
                    elif resp.getcode() != 200: 
                        rows[3] = down
                    else: 
                        rows[3] = up
                except: 
                    rows[3] = down #print traceback.format_exc()

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
