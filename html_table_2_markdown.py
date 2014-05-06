#!/usr/local/bin/python

import argparse
import os
import os.path
import shutil
from bs4 import BeautifulSoup
from sys import argv, exit

def parse_cell(el):
    return el.text.strip().replace("\n", " ").replace("&#160;", "")

def parse_row(el):
 	return [parse_cell(td) for td in el.find_all("td")]

def parse_table(el):
 	return [parse_row(tr) for tr in el.tbody.find_all("tr")]

def get_correctedFiles(path, save):
    if not os.path.exists(save):
        os.makedirs(save)

    for f in os.listdir(path):
        print "converting html tables to markdown (text) in file %s" % f
        infile = open(os.path.join(path, f)).read()

        # rules for converting a table to markdown
        tree = BeautifulSoup(infile, "html5lib")

        for table in tree.find_all("table"):
            parsed = parse_table(table)
            table.clear()
            for row in parsed:
                line = u" | ".join(row)
                table.append(tree.new_tag("br"))
                table.append(line)
            table.name = u"div"

        infile = tree.prettify()

        outfile = open(os.path.join(save, f), "w")
        outfile.write(infile.encode("ascii", "xmlcharrefreplace"))
        outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="removes all bad bold and italic markup")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("save", help="folder to save no table html (edited) files")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_correctedFiles(args.path, args.save):
        print "Error"
    else:
        print "Done"
