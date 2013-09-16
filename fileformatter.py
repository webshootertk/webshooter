#!/usr/local/bin/python

import shutil
import os
import os.path
from htmlcleaner import filtered_text
from bs4 import BeautifulSoup   

path = "/Users/harris112/Projects/aims-group/uvcdat-site/wiki"
backup = "/Users/harris112/Projects/aims-group/uvcdat-site/wiki/zHTML"

topfile = 131
bottomfile = 56

for root, _, files in os.walk(path):
    for f in files:
        extension = os.path.splitext(f)[1]
        if extension not in (".md", ".py", ".pyc"):
            infile = open(os.path.join(root, f)).readlines()

            infile = infile[topfile:-1*bottomfile]
            cleaned = []
            for line in infile:
                line = line.strip()
                line = ">\n".join(line.split(">"))
                
                cleaned.append(line)

            clean_string = "\n".join(cleaned)
            cleaned_soup = BeautifulSoup(clean_string, "html5lib")
            clean_string = filtered_text(cleaned_soup.body, ["a"])
            cleaner_string = ''
            for line in clean_string.split("\n"):
                line = line.strip()
                if len(line):
                    cleaner_string += "%s\n" % line
            
            outfile = open(f + ".md", "w")
            outfile.write(cleaner_string.encode("ascii", "xmlcharrefreplace"))
            outfile.close()

            shutil.move(os.path.join(root, f), backup)
