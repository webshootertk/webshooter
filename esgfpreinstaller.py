#!/usr/local/python

import os
import os.path
import platform
import rpm
import shutil
import subprocess
import sys
import yum

required_packages = [
# esgf
"autoconf",
"automake",
"bison-devel",
"expat-devel",
"file",
"flex",
"gcc",
"gcc-c++",
"gettext-devel",
"git",
"libtool-ltdl-devel",
"libuuid-devel",
"libxml2-devel",
"libxslt-devel",
"lsof",
"make",
"openssl-devel",
"pam-devel",
"pax",
"pax-utils",
"perl-Archive-Tar",
"perl-XML-Parser",
"readline-devel",
"tk-devel",
"wget",
"zlib-devel",
# uvcadt / linux
"gcc-gfortran",
"gdbm-devel",
"libdbi-devel",
"libgfortran",
"libpng-devel",
"libqtxdg-devel",
"libXt-devel",
"PyQt4-devel",
"qt-devel",
"sqlite-devel",
"tcl-devel",
"tcllib",
# uvcadt / centos
"bzip2-devel",
"dbus-devel",
"dbus-c++-devel",
"dbus-glib-devel",
"gtkglext-devel",
"mesa-libGL-devel",
"mesa-libGLU-devel",
"PyOpenGL",  #OpenGL
"gstreamer-devel",
"libcurl-devel",
"openssl-devel",
# get all the packages!!
"gstreamer-plugins-good-devel",
"gstreamer-plugins-bad-free-devel",
"gstreamer-plugins-bad-free-extras",
"gstreamer-plugins-base-devel",
"gstreamer-plugins-base-devel-docs",
#
"perl-ExtUtils-AutoInstall",
"perl-ExtUtils-CBuilder",
"perl-ExtUtils-CChecker",
"perl-ExtUtils-Config",
"perl-ExtUtils-Depends",
"perl-ExtUtils-Embed",
"perl-ExtUtils-F77",
"perl-ExtUtils-H2PM",
"perl-ExtUtils-Helpers",
"perl-ExtUtils-InstallPaths",
"perl-ExtUtils-MakeMaker",
"perl-ExtUtils-MakeMaker-Coverage",
"perl-ExtUtils-ParseXS",
"perl-ExtUtils-PkgConfig",
"perl-ExtUtils-XSBuilder",
#
"xorg-x11-apps",
"xorg-x11-docs",
"xorg-x11-drivers",
"xorg-x11-drv-acecad",
"xorg-x11-drv-aiptek",
"xorg-x11-drv-apm",
"xorg-x11-drv-ast",
"xorg-x11-drv-ati",
"xorg-x11-drv-ati-firmware",
"xorg-x11-drv-cirrus",
"xorg-x11-drv-dummy",
"xorg-x11-drv-elographics",
"xorg-x11-drv-evdev-devel",
"xorg-x11-drv-fbdev",
"xorg-x11-drv-fpit",
"xorg-x11-drv-glint",
"xorg-x11-drv-hyperpen",
"xorg-x11-drv-i128",
"xorg-x11-drv-i740",
"xorg-x11-drv-intel-devel",
"xorg-x11-drv-keyboard",
"xorg-x11-drv-mach64",
"xorg-x11-drv-mga",
"xorg-x11-drv-modesetting",
"xorg-x11-drv-mouse-devel",
"xorg-x11-drv-mutouch",
"xorg-x11-drv-nouveau",
"xorg-x11-drv-nv",
"xorg-x11-drv-openchrome-devel",
"xorg-x11-drv-penmount",
"xorg-x11-drv-qxl",
"xorg-x11-drv-r128",
"xorg-x11-drv-rendition",
"xorg-x11-drv-s3virge",
"xorg-x11-drv-savage",
"xorg-x11-drv-siliconmotion",
"xorg-x11-drv-sis",
"xorg-x11-drv-sisusb",
"xorg-x11-drv-synaptics-devel",
"xorg-x11-drv-tdfx",
"xorg-x11-drv-trident",
"xorg-x11-drv-v4l",
"xorg-x11-drv-vesa",
"xorg-x11-drv-vmmouse",
"xorg-x11-drv-vmware",
"xorg-x11-drv-void",
"xorg-x11-drv-voodoo",
"xorg-x11-drv-wacom-devel",
"xorg-x11-drv-xgi",
"xorg-x11-font-utils",
"xorg-x11-fonts-100dpi",
"xorg-x11-fonts-75dpi",
"xorg-x11-fonts-ISO8859-1-100dpi",
"xorg-x11-fonts-ISO8859-1-75dpi",
"xorg-x11-fonts-ISO8859-14-100dpi",
"xorg-x11-fonts-ISO8859-14-75dpi",
"xorg-x11-fonts-ISO8859-15-100dpi",
"xorg-x11-fonts-ISO8859-15-75dpi",
"xorg-x11-fonts-ISO8859-2-100dpi",
"xorg-x11-fonts-ISO8859-2-75dpi",
"xorg-x11-fonts-ISO8859-9-100dpi",
"xorg-x11-fonts-ISO8859-9-75dpi",
"xorg-x11-fonts-Type1",
"xorg-x11-fonts-cyrillic",
"xorg-x11-fonts-ethiopic",
"xorg-x11-fonts-misc",
"xorg-x11-proto-devel",
"xorg-x11-resutils",
"xorg-x11-server-Xdmx",
"xorg-x11-server-Xephyr",
"xorg-x11-server-Xnest",
"xorg-x11-server-Xorg",
"xorg-x11-server-Xvfb",
"xorg-x11-server-common",
"xorg-x11-server-devel",
"xorg-x11-server-source",
"xorg-x11-server-utils",
"xorg-x11-twm",
"xorg-x11-util-macros",
"xorg-x11-utils",
"xorg-x11-xauth",
"xorg-x11-xbitmaps",
"xorg-x11-xdm",
"xorg-x11-xinit",
"xorg-x11-xinit-session",
"xorg-x11-xkb-extras",
"xorg-x11-xkb-utils-devel",
"xorg-x11-xtrans-devel",
]

stack_packages = [
#  GET REAL JAVA7 --> "java7",
"tomcat",
"python",
"psql"
]

system_packages = []
missing_packages = []

FNULL = open(os.devnull, 'w')

def check_os():
  print platform.node()
  print platform.platform()
  print " "
  # check for correct os

def check_user():
  user_id = subprocess.call(["id", "-u", "esg-user"], stdout=FNULL, stderr=subprocess.STDOUT)
  if user_id: print "We recommend creating and using an esg-user account for this install"
  else: print "esg-user found"
  print " "  

def check_host_domain_names():
  subprocess.call(["hostname", "-s"])
  subprocess.call(["hostname", "--domain"])
  subprocess.call(["hostname", "--fqdn"])
  print " "

def check_packages():
  trans = rpm.TransactionSet()
  for header in trans.dbMatch():
    system_packages.append(header['name'])
    if header['name'] == "openssl-devel":
     version =  header['version'].split(".")
     release = int(version[0])
     if release >= 1:
        print "Openssl version higher than 1.0.0 may lead to problems, consider down grading.\nhttp://esgf.org/bugzilla/show_bug.cgi?id=123"
        print" "
    
  global required_packages
  for package in required_packages:
    global missing_packages
    if package not in system_packages:
      missing_packages.append(package)
  
def check_stack():
  global missing_packages
  for stacks in stack_packages:
    output = subprocess.call(["which", stacks], stdout=FNULL, stderr=subprocess.STDOUT)
    if output:  
      if stacks == "psql": stacks = " postgresql-devel"
      missing_packages.append(stacks)
    else: 
      if stacks == "tomcat6":
        print "tomcat info:"
        subprocess.call([stacks, "version"])
      else: 
        if stacks =="python":
          print "python info:"
          print "Python 2.7.6 or higher is required"
        if stacks == "psql":
          print "postgres info:"
        subprocess.call([stacks, '--version'])
    print ""

def print_findings():
  if len(missing_packages) == 0:
    print "no missing packages"
  else:
    total_required = len(required_packages)
    total_missing = len(missing_packages)
    missing = " ".join(missing_packages)
    print "missing %d of %d packages" % (total_missing, total_required)
    print "try installing  with yum:"
    print "sudo yum install %s" % missing
    print " "
    print "Another quick fix it sudo yum install xorg*"
    print "yum install autoconf automake bison file flex gcc gcc-c++ gettext-devel libtool libuuid-devel libxml2 libxml2-devel libxslt libxslt-devel lsof make openssl-devel pam-devel pax readline-devel tk-devel wget zlib-devel *ExtUtils* perl-Archive-Tar perl-XML-Parser gcc-gfortran ntp xorg*"
    
    print " "
    print "if yum can not find any of these packages you may need add the epel repo to your yum repo list.\nhttp://www.thegeekstuff.com/2012/06/enable-epel-repository"
  print " "

def get_esgfbootstrap():
  #TODO: complete a full preinstall by setting up for install
  print ""

if __name__ == "__main__":

  check_os()
  check_user()
  check_host_domain_names()
  check_packages()
  check_stack()
  print_findings()
  get_esgfbootstrap()
  print "done"
