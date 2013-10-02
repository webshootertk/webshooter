#!/usr/local/bin/python

import shutil
import os
import os.path
import argparse
import sys
import subprocess
import setuptools
import yum

packages = [ 
            "autoconf",
            "automake",
            "bison-devel",
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
            "readline-devel",
            "tk-devel",
            "wget",
            "zlib-devel",
            #perl-ExtUtils*
            "perl-Archive-Tar",
            "perl-XML-Parser",
            #xorg-x11*
            ]

missing_packages = []

def check_packages():
    for package in packages:
        is_package = subprocess.call(["which", package])
        
        if is_package:
            global missing_packages
            missing_packages.append(package)
    
    if len(missing_packages) == 0:
        print "no missing packages"
    else:
        missing = " ".join(missing_packages)
        print "missing the following packages:\n%s\nTry:" % missing
        print "    yum search package"
        print "    yum install package-devel (if devel option exists)"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="will determine if this system is ready to run the ESGF installer")
    parser.add_argument("--preserve", "-p", help="report type html or md")

    args = parser.parse_args()

    print "os.name: %s" % os.name
    print os.uname()
    print "sys.platform: %s" % sys.platform
    print " "
    # check for correct os

    if check_packages():
        print "Error"
    else:
        print "Done"
    yb = yum.YumBase()
    if yb.rpmdb.searchNevra(name='make'):
        print "installed"
    else:
        print "not installed"
#perl-ExtUtils-AutoInstall
#perl-ExtUtils-CBuilder
#perl-ExtUtils-CChecker
#perl-ExtUtils-Config
#perl-ExtUtils-Depends
#perl-ExtUtils-Embed
#perl-ExtUtils-F77
#perl-ExtUtils-H2PM
#perl-ExtUtils-Helpers
#perl-ExtUtils-InstallPaths
#perl-ExtUtils-MakeMaker
#perl-ExtUtils-MakeMaker-Coverage
#perl-ExtUtils-ParseXS
#perl-ExtUtils-PkgConfig
#perl-ExtUtils-XSBuilder

#xorg-x11-apps
#xorg-x11-docs
#xorg-x11-drivers
#xorg-x11-drv-acecad
#xorg-x11-drv-aiptek
#xorg-x11-drv-apm
#xorg-x11-drv-ast
#xorg-x11-drv-ati
#xorg-x11-drv-ati-firmware
#xorg-x11-drv-cirrus
#xorg-x11-drv-dummy
#xorg-x11-drv-elographics
#xorg-x11-drv-evdev-devel
#xorg-x11-drv-fbdev
#xorg-x11-drv-fpit
#xorg-x11-drv-glint
#xorg-x11-drv-hyperpen
#xorg-x11-drv-i128
#xorg-x11-drv-i740
#xorg-x11-drv-intel-devel
#xorg-x11-drv-keyboard
#xorg-x11-drv-mach64
#xorg-x11-drv-mga
#xorg-x11-drv-modesetting
#xorg-x11-drv-mouse-devel
#xorg-x11-drv-mutouch
#xorg-x11-drv-nouveau
#xorg-x11-drv-nv
#xorg-x11-drv-openchrome-devel
#xorg-x11-drv-penmount
#xorg-x11-drv-qxl
#xorg-x11-drv-r128
#xorg-x11-drv-rendition
#xorg-x11-drv-s3virge
#xorg-x11-drv-savage
#xorg-x11-drv-siliconmotion
#xorg-x11-drv-sis
#xorg-x11-drv-sisusb
#xorg-x11-drv-synaptics-devel
#xorg-x11-drv-tdfx
#xorg-x11-drv-trident
#xorg-x11-drv-v4l
#xorg-x11-drv-vesa
#xorg-x11-drv-vmmouse
#xorg-x11-drv-vmware
#xorg-x11-drv-void
#xorg-x11-drv-voodoo
#xorg-x11-drv-wacom-devel
#xorg-x11-drv-xgi
#xorg-x11-font-utils
#xorg-x11-fonts-100dpi
#xorg-x11-fonts-75dpi
#xorg-x11-fonts-ISO8859-1-100dpi
#xorg-x11-fonts-ISO8859-1-75dpi
#xorg-x11-fonts-ISO8859-14-100dpi
#xorg-x11-fonts-ISO8859-14-75dpi
#xorg-x11-fonts-ISO8859-15-100dpi
#xorg-x11-fonts-ISO8859-15-75dpi
#xorg-x11-fonts-ISO8859-2-100dpi
#xorg-x11-fonts-ISO8859-2-75dpi
#xorg-x11-fonts-ISO8859-9-100dpi
#xorg-x11-fonts-ISO8859-9-75dpi
#xorg-x11-fonts-Type1
#xorg-x11-fonts-cyrillic
#xorg-x11-fonts-ethiopic
#xorg-x11-fonts-misc
#xorg-x11-proto-devel
#xorg-x11-resutils
#xorg-x11-server-Xdmx
#xorg-x11-server-Xephyr
#xorg-x11-server-Xnest
#xorg-x11-server-Xorg
#xorg-x11-server-Xvfb
#xorg-x11-server-common
#xorg-x11-server-devel
#xorg-x11-server-source
#xorg-x11-server-utils
#xorg-x11-twm
#xorg-x11-util-macros
#xorg-x11-utils
#xorg-x11-xauth
#xorg-x11-xbitmaps
#xorg-x11-xdm
#xorg-x11-xinit
#xorg-x11-xinit-session
#xorg-x11-xkb-extras
#xorg-x11-xkb-utils-devel
#xorg-x11-xtrans-devel
