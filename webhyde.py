import shutil
import site
import yaml
from webreplace import replace

class HydeSite(object):
  def __init__(self):
    self.shortname = None
    self.hyde_template  = None
    self.color     = None
    self.site_yaml = dict()
    self.site_yaml["context"] = dict()
    self.site_yaml["context"]["data"] = dict()
    self.site_yaml["context"]["data"]["menu"] = list()
    self.site_yaml["context"]["data"]["site_title"] = None

  @property
  def longname(self):
    return self.site_yaml["context"]["data"]["site_title"]

  @longname.setter
  def longname(self, value):
    self.site_yaml["context"]["data"]["site_title"] = value

  @property
  def pages(self):
    return self.site_yaml["context"]["data"]["menu"]

  @pages.setter
  def pages(self, pages):
    for p in pages:
      filename = p.lower().replace(" ", "-") + ".html"
      self.site_yaml["context"]["data"]["menu"].append({"title": p, "url": filename})
      shutil.copy(self.shortname + "/content/blank.html", self.shortname + "/content/" + filename)
      replace(self.shortname + "/content/" + filename, "Page name", p)

  @property
  def yaml(self):
    self.site_yaml["context"]["data"]["author"] = dict()
    self.site_yaml["plugins"] = list()
    self.site_yaml["mode"] = "development"
    self.site_yaml["media_url"] = "media"
#   self.site_yaml["context"]["data"]["author"]["name"] = getpass.getuser()
    self.site_yaml["context"]["data"]["nav_hover"] = True
    self.site_yaml["context"]["data"]["home_url"] = "index.html"
    self.site_yaml["plugins"].append("hyde.ext.plugins.meta.MetaPlugin")
    self.site_yaml["plugins"].append("hyde.ext.plugins.auto_extend.AutoExtendPlugin")
    self.site_yaml["plugins"].append("hyde.ext.plugins.syntext.SyntextPlugin")
    self.site_yaml["plugins"].append("hyde.ext.plugins.textlinks.TextlinksPlugin")
    self.site_yaml["context"]["data"]["menu"].append({"title": "Home", "url": "index.html"})
    return yaml.dump(self.site_yaml)
