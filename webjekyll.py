import shutil
import site
import pdb
from webreplace import replace

class JekyllSite(object):
  def __init__(self):
    self.shortname = None
    self.longname = None
    self.jekyll_templates = None
    self.track = list()

  @property
  def pages(self):
    return self.track

  @pages.setter 
  def pages(self, pages):
    for p in pages:
      self.pages.append({"title": p, "url": p})
      shutil.copy(self.shortname + "/blank.md", self.shortname + "/" + p + ".md")
      replace(self.shortname + "/" + p + ".md", "Blank", p)

def cleanup(self):
  lines = open(self.shortname + "/" + "blank.md", "r").readlines()
  del lines[3]
  open(self.shortname + "/" + "blank.md", "w").writelines(lines)
