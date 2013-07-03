#!/usr/bin/env python3

import getpass
import os
import re
import shutil
import subprocess
import sys
import yaml

cfg = dict()

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
             3: ("bootstrap", "github.com/aims-group/hyde-bootstrap")}
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

run_prompt = """Site generation complete! Start a server on port 8080 now? If you don't, you'll
have to cd into your site's directory and manually run `hyde gen` and, if you
want a miniserver running, `hyde serve`. [y/N] """

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
    cfg["longname"] = ""
    while cfg["longname"] is "":
      cfg["longname"] = input("longname> ").strip()
# shortname
    print(shortname_prompt)
    cfg["shortname"] = ""
    while cfg["shortname"] is "":
      cfg["shortname"] = input("shortname> ").strip()
      if re.search("\s", cfg["shortname"]) is not None:
        cfg["shortname"] = ""
        print("The shortname cannot have spaces, try again.")
      if os.path.exists(cfg["shortname"]):
        if input("A file/folder named " + cfg["shortname"] + " already exists here. Delete the whole thing [y/N]? ").lower() == 'y':
          shutil.rmtree(cfg["shortname"])
        else:
          cfg["shortname"] = ""
# Description
    print(description_prompt)
    cfg["description"] = ""
    while cfg["description"] is "":
      cfg["description"] = input("description> ").strip()
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
#    if template[0] is "tshirt" or template[0] is "bootstrap":
#      print(color_prompt)
#      cfg["color"] = ""
#      while cfg["color"] is "":
#        cfg["color"] = input("color> #").strip()
# Pages
    print(pages_prompt)
    pages = ""
    while pages is "":
      pages = [ p.strip() for p in input("pages> ").split(",") ]
# Logo
#    print(logo_prompt)
#    cfg["logo"] = input("logo> ").strip()

# Set up the site
    subprocess.call(["git", "clone", "git://" + template[1], cfg["shortname"]])
    site = dict()
    site["context"] = dict()
    site["context"]["data"] = dict()
    site["context"]["data"]["author"] = dict()
    site["context"]["data"]["menu"] = list()
    site["plugins"] = list()
    site["mode"] = "development"
    site["media_root"] = "media"
    site["media_url"] = "/media"
    site["context"]["data"]["site_title"] = cfg["longname"]
    site["context"]["data"]["author"]["name"] = getpass.getuser()
    site["context"]["data"]["home_url"] = "index.html"
    site["plugins"].append("hyde.ext.plugins.meta.MetaPlugin")
    site["plugins"].append("hyde.ext.plugins.auto_extend.AutoExtendPlugin")
    site["plugins"].append("hyde.ext.plugins.syntext.SyntextPlugin")
    site["plugins"].append("hyde.ext.plugins.textlinks.TextlinksPlugin")
    for p in pages:
      filename = p.lower().replace(" ", "-") + ".html"
      site["context"]["data"]["menu"].append({"title": p, "url": filename})
      shutil.copy(cfg["shortname"] + "/content/index.html", cfg["shortname"] + "/content/" + filename)
    f = open(cfg["shortname"] + "/site.yaml", "w")
    f.write(yaml.dump(site))

    if input(run_prompt).lower() == "y":
      subprocess.Popen(["hyde", "gen"], cwd=os.getcwd() + "/" + cfg["shortname"])
      subprocess.Popen(["hyde", "serve"], cwd=os.getcwd() + "/" + cfg["shortname"])

  elif sys.argv[1] == "update":
    cfg["shortname"] = sys.argv[2]
    f = open(cfg["shortname"] + "/site.yaml")
    yaml = cfg = yaml.load(f)

def check_deps():
# python3
# hyde
#   if not, pip
  pass

def set_up_hyde():
  pass
