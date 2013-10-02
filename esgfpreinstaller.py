#!/usr/local/bin/python

import shutil
import os
import os.path
import argparse
import sys
import subprocess

packages = [ 
            "autoconf",
            "automake",
            "bison",
            "file",
            "flex",
            "gcc",
            "gcc-c++",
            "gettext",
            "libtool",
            "libuuid",
            "libzml2",
            "libxslt",
            "lsof",
            "make",
            "openssl",
            "pam",
            "pax",
            "readline",
            "tk",
            "wget",
            "zlib"
            ]

missing_packages = []

def check_packages():
    for package in packages:
        is_package = subprocess.call(["which", package])
        # /usr/local/bin
        # /usr/bin
        # /usr/sbin
        # /bin/
        
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




