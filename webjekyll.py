import shutil
import site
from webreplace import replace

class JekyllSite:
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
      filename = p.lower().replace(" ", "-") + ".md"
      self.pages.append({"title": p, "url": filename})
      shutil.copy(self.shortname + "/blank.md", self.shortname + "/" + filename)
      replace(self.shortname + "/" + filename, "Blank", p)

