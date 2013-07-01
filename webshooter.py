#!/usr/bin/env python3

import os
import re
import subprocess
import sys

longname_prompt = """Your website will have two names.
The longname is what users will see. It can have spaces.
A good longname is 'My First Website'. Enter the longname now."""

shortname_prompt = """The shortname is used to name the site on the back end. By convention it should
be lowercase and use hyphens as spaces. A good shortname is 'my-first-website'.
Enter the shortname now."""

description_prompt = """The description is displayed in your site's header, below the longname. Enter
the description now."""

templates = {1: ("one.5lab",  "github.com/aims-group/one.5lab"),
             2: ("tshirt",    "github.com/aims-group/tshirt"),
             3: ("bootstrap", "github.com/aims-group/bootstrap")}
template_prompt = "What template to use?"
for k,t in templates.items():
  template_prompt += "\n  " + str(k) + ": " + t[0] + " (" + t[1] + ")"

color_prompt = """You can choose a dominate color to use for this template. Enter one in hex color
format (#RRGGBB)."""

pages_prompt = """What pages will exist?
  You can change these later. Do not include external links you want in nav.
  Separate pages with commas. Enter pages in longname format; shortnames will be
  generated automatically."""

logo_prompt = """Specify a path to a logo which will be copied to your site's directory. If you
don't have one yet, just press Return."""

if len(sys.argv) < 2 or sys.argv[1] == "--help":
  print(
  """usage: """ + sys.argv[0] + """ new
       """      + sys.argv[0] + """ update"""
  )
else:
  if sys.argv[1] == "new":
# longname
    print(longname_prompt)
    cin = None
    longname = ""
    while longname is "":
      longname = input("longname> ").strip()
# shortname
    print(shortname_prompt)
    shortname = ""
    while shortname is "":
      shortname = input("shortname> ").strip()
      if re.search("\s", shortname) is not None:
        shortname = ""
        print("The shortname cannot have spaces, try again.")
# Description
    print(description_prompt)
    description = ""
    while description is "":
      description = input("description> ").strip()
# Template
    print(template_prompt)
    template = ""
    while template not in templates:
      try:
        template = int(input("template> ").strip())
      except ValueError:
        pass
    template = templates[template]
# Color (if tshirt or bootstrap)
    if template[0] is "tshirt" or template[0] is "bootstrap":
      print(color_prompt)
      color = ""
      while color is "":
        color = input("color> #").strip()
# Pages
    print(pages_prompt)
    pages = ""
    while pages is "":
      pages = [ p.strip() for p in input("pages> ").split(",") ]
# Logo
    print(logo_prompt)
    logo = input("logo> ").strip()

# Set up the site
    subprocess.call(["git", "clone", "git://" + template[1]])
  elif sys.argv[1] == "update":
    print("Not implemented yet")

def check_deps():
# python3
# hyde
#   if not, pip
  pass

def set_up_hyde():
  pass
