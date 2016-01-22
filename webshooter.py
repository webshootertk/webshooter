#!/usr/bin/env python2

import getpass
import os
import re
import shutil
import site
import subprocess
import sys
import tempfile
import time
import yaml
from webreplace import replace
from webhyde import HydeSite
from webjekyll import JekyllSite
from webjekyll import cleanup

if sys.version_info[0] == 3:
  if raw_input("""I was written in Python 2.x, but you're running me with Python 3.x! I was NOT
tested with this version. Run anyway? [y/N] """).lower() != "y":
    sys.exit()


options = {1: "Hyde",
           2: "Jekyll"}
options_prompt = "What static website generator to use?"
for k,t in options.items():
    options_prompt += "\n " + str(k) + ": " + t

longname_prompt = """Your website will have two names.
The longname is what users will see. It can have spaces.
A good longname is 'My First Website'. Enter the longname now."""

shortname_prompt = """The shortname is used to name the site on the back end. By convention it should
be lowercase and use hyphens as spaces. A good shortname is 'my-first-website'.
Enter the shortname now."""

description_prompt = """The description is displayed in your site's header, below the longname. Enter
the description now."""

hyde_templates = {1: ("bootstrap", "github.com/webshootertk/hyde-bootstrap.git"),
                  2: ("one.5lab",  "github.com/webshootertk/hyde-one.5lab.git"),
                  3: ("tshirt",    "github.com/webshootertk/hyde-tshirt.git")}
hyde_template_prompt = "What template to use?"
for k,t in hyde_templates.items():
  hyde_template_prompt += "\n  " + str(k) + ": " + t[0] + " (" + t[1] + ")"

jekyll_templates = {1: ("bootstrap", "github.com/webshootertk/jekyll-bootstrap.git"),
                    2: ("one.5lab",  "github.com/webshootertk/jekyll-one.5lab.git"),
                    3: ("tshirt",    "github.com/webshootertk/jekyll-tshirt.git")}
jekyll_template_prompt = "What template to use?"
for k,t in jekyll_templates.items():
  jekyll_template_prompt += "\n  " + str(k) + ": " + t[0] + " (" + t[1] + ")"


pages_prompt = """What pages will exist?
  You can change these later. Do not include external links you want in nav.
  Separate pages with commas. Enter pages in longname format; shortnames will be
  generated automatically."""

set_null = open(os.devnull, 'w')

def hyde_gen(path):
  subprocess.Popen(["hyde", "gen"], cwd=path, stdout=set_null)
  replace(path + '/.git/config', 'origin', 'upstream')
  print("Complete! Now open\n\n  " + os.path.abspath(path) + "/deploy/index.html\n\nin a web browser.\n")
  print("To keep your site style up to date you can run\n\n  git pull upstream master\n") 

def jekyll_build(path):
  subprocess.Popen(["jekyll", "build"], cwd=path, stdout=set_null)
  replace(path + '/.git/config', 'origin', 'upstream')
  print("Complete! Now open\n\n  " + os.path.abspath(path) + "/_site/index.html\n\nin a web browser.\n")
  print("To keep your site style up to date you can run\n\n  git pull upstream master\n") 


if len(sys.argv) < 2 or sys.argv[1] == "--help":
  print(
  """usage: """ + sys.argv[0] + """ <command> [--help]

commands:
  new              Interactively create a new website
  gen <site_path>  Regenerate a Hyde site at `site_path`
  build <site_path Regenerate a Jekyll site at 'site_path'"""
  )
elif ( len(sys.argv) is 3 and sys.argv[2] == "--help" ) or ( len(sys.argv) is 2 and sys.argv[1] == "gen" ):
  if sys.argv[1] == "new":
    print("""usage: """ + sys.argv[0] + """ new [--help]

  Runs an interactive prompt to create a new website using webshooter. Asks for
  website information such as longname, shortname, template, and a list of pages.
  When the process is complete, the desired template will be cloned into the
  current working directory and your settings for the site will be applied. At
  this point, you should go into this new directory and change the pages in
  the `content` directory to your liking.

  Whenever you change the content of the website and wish for it to be
  regenerated, use `""" + sys.argv[0] + """ gen`.""")
  elif sys.argv[1] == "gen":
    print("""usage: """ + sys.argv[0] + """ gen <site_path>
       """ + sys.argv[0] + """ gen --help

  Regenerates the static content for the website at `site_path` using hyde. You
  should run this whenever any changes are made to the site that you wish to be
  reflected in the deployed version.

  To make changes, edit the files in `layout` and `content`, as well as
  `site.yaml`. After running """ + sys.argv[0] + """, these changes will be
  reflected in the `deploy` directory.""")

else:
  if sys.argv[1] == "new":

    template = ""
    color = ""
    pages = ""
    static = ""

# option
    print(options_prompt)
    while static not in {"1", "2"}:
      try:
        static = str(input("option> ")).strip()
      except (KeyError, ValueError):
        pass

    if static is "1":
      site = HydeSite()
    elif static is "2":
      print("Jekyll")
      site = JekyllSite()
    else:
      print("FAIL")
      sys.exit("o gosh should never see this")

# longname
    print(longname_prompt)
    while not bool(site.longname):
      site.longname = raw_input("longname> ").strip()

# shortname
    print(shortname_prompt)
    while not bool(site.shortname):
      site.shortname = raw_input("shortname> ").strip()
      if re.search("\s", site.shortname) is not None:
        site.shortname = ""
        print("The shortname cannot have spaces, try again.")
      elif os.path.exists(site.shortname):
        if raw_input("A file/folder named " + site.shortname + " already exists here. Delete the whole thing [y/N]? ").lower() == 'y':
          shutil.rmtree(site.shortname)
        else:
          site.shortname = ""

# Template
    if static is "1":
      print(hyde_template_prompt)
      while site.hyde_template not in hyde_templates.values():
        try:
          site.hyde_template = hyde_templates[int(raw_input("template> ").strip())]
        except (KeyError, ValueError):
          pass
      subprocess.call(["git", "clone", "git://" + site.hyde_template[1], site.shortname])
    elif static is "2":
      print(jekyll_template_prompt)
      while site.jekyll_templates not in jekyll_templates.values():
        try:
          site.jekyll_templates = jekyll_templates[int(raw_input("template> ").strip())]
        except (KeyError, ValueError):
          pass
      subprocess.call(["git", "clone", "git://" + site.jekyll_templates[1], site.shortname])

    else:
      print("FAIL")
      sys.exit("o gosh should never see this")


# Pages
    print(pages_prompt)
    while not bool(site.pages):
      site.pages = [ p.strip() for p in raw_input("pages> Home, ").split(",") ]

# Set up the site
    if static is "1":
      replace(site.shortname + "/content/index.html", "Page name", "Home")
      open(site.shortname + "/site.yaml", "w").write(site.yaml)
      hyde_gen(os.getcwd() + "/" + site.shortname)
    elif static is "2":
      replace(site.shortname + "/index.md", "Page name", "Home")
      jekyll_build(os.getcwd() + "/" + site.shortname)
    elif sys.argv[1] == "gen":
      hyde_gen(sys.argv[2])
    elif sys.argv[1] == "build":
        jekyll_build(sys.argv[2])

# Cleanup
    subprocess.call(["rm", "-rf", "__pycache__"])

def check_deps():
  python3
  hyde
  if not pip:
    pass

def set_up_hyde():
  pass

if static is "2":
    cleanup(site);

