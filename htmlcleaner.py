#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup
from bs4.element import Tag, Comment
import os.path
from sys import stderr, exit

__ugly_tags__ = ["script", "noscript", "embed", "object", "iframe"]

def is_tag(tag):
	return isinstance(tag, Tag)

def __filter_text__(tag, allowed_tags, validator):
	if isinstance(tag, Comment):
		print "Removing comment"
		tag.extract()
		return

	if validator:
		if validator(tag) is False:
			tag.extract()
			return

	if tag.name in __ugly_tags__:
		tag.extract()
		return

	for child in tag.children:
		if is_tag(child):

			__filter_text__(child, allowed_tags, validator)
			
			if child.parent is None:
				continue

			if allowed_tags and child.name in allowed_tags:
				continue
			else:
				child.unwrap()
		else:
			if isinstance(child, Comment):
				child.extract()
				continue
			child.replace_with(unicode(child))


def filtered_text(tag, allowed_tags, validator=None):
	if not is_tag(tag):
		return tag

	#Don't modify the tree
	new_tree = BeautifulSoup(tag.prettify(formatter="html"), "html5lib")

	actual_tag = new_tree.body

	__filter_text__(actual_tag, allowed_tags, validator)

	text = ''

	for child in actual_tag:
		if is_tag(child):
			text += child.prettify(formatter="html")
		else:
			if isinstance(child, Comment):
				continue
			text += child

	return text.strip()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='extracts text from body of an HTML document')
	parser.add_argument("infile", help="path to html (raw) files")
	parser.add_argument("outfile", help="path to desired output file")
	parser.add_argument("--preserve", "-p", action="append", help="repeatable parameter that adds a tag name to preserve (e.g. htmlcleaner.py -p a -p img)")

	args = parser.parse_args()
	
	if not os.path.exists(args.infile):
		stderr.write("Input file %s not found." % args.infile)
		exit()

	infile = open(args.infile)
	infile_contents = infile.read()
	infile.close()
	insoup = BeautifulSoup(infile_contents, "html5lib")

	filtered = filtered_text(insoup.body, args.preserve).encode("ascii", "xmlcharrefreplace")

	out = open(args.outfile, "w")
	out.write(filtered)
	out.close()
