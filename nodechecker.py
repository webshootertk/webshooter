#!/usr/local/bin/python

import subprocess
import urllib
import shutil
import argparse
import os
import os.path
import traceback
from sys import argv, exit

path = "/Users/harris112/Projects/ESGF/esgf.github.io.wiki"
path_to_file = "/Users/harris112/Projects/ESGF/esgf.github.io.wiki/Shutdown-Status.md"
node = "Node "
faq = "question "
node_manager = "esgf-node-manager"
esgf_web_fe = "esgf-web-fe"
thredds = "thredds"
askbot = "Askbot"
rows = []
urls = []
newfile = []
end_file_flag = False

#subprocess.call(["cd", path])
#subprocess.call(["git", "pull"])

infile = open(path_to_file).readlines()
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
                url = rows[1].strip()
                if not url: rows[3] = " down"
                else:
                    try:
                        print url
                        resp = urllib.urlopen(url)
                        code = resp.next()
                        if node_manager not in code and esgf_web_fe not in code and thredds not in code: rows[3] = " down"
                        elif resp.getcode() != 200: rows[3] = " down"
                        else: rows[3] = " up"
                    except: rows[3] = " down" #print traceback.format_exc()

                temp =  "|".join(rows)
                newfile.append(temp)
        else: newfile.append(line)

#outfile = open("test.txt", "w")
outfile = open(path_to_file, "w")
outfile.write("\n".join(newfile))
outfile.close()

#subprocess.call(["git", "commit", "-am", "\"BOT: AUTO UPDATE NODE STATUS\""])
#subprocess.call(["git", "pull"])
#subprocess.call(["git", "push"])

print "done"
