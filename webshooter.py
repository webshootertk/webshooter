#!/usr/bin/env python3

import sys


if (len(sys.argv) < 2 or sys.argv[1] == "--help"):
  print (
  """usage: """ + sys.argv[0] + """ new
       """ + sys.argv[0] + """ update"""
  )
else:
  if (sys.argv[1] == "new"):
    print ("Making new site...")
  if (sys.argv[1] == "update"):
    print ("Updating site...")
