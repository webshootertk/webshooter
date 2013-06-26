#!/usr/bin/env python3

import os
import re
import sys

frontname_prompt = """Your website will have two names.
The frontname is what users will see. It can have spaces.
A good frontname is 'My First Website'. Enter the frontname now."""

backname_prompt = """The backname is used to name the site on the back end. By convention it should
be lowercase and use hyphens as spaces. A good backname is 'my-first-website'.
Enter the backname now."""

description_prompt = """The description is displayed in your site's header, below the frontname. Enter
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
  Separate pages with commas. Enter pages in frontname format; backnames will be
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
# Frontname
    print(frontname_prompt)
    cin = None
    frontname = ""
    while frontname is "":
      frontname = input("frontname> ").strip()
# Backname
    print(backname_prompt)
    backname = ""
    while backname is "":
      backname = input("backname> ").strip()
      if re.search("\s", backname) is not None:
        backname = None
        print("The backname cannot have spaces, try again.")
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
    logo = ""
    while logo is "" or not os.path.exists(logo):
      logo = input("logo> ").strip()
  elif sys.argv[1] == "update":
    print("Not implemented yet")

def check_deps():
# python3
# hyde
#   if not, pip

def set_up_hyde():
