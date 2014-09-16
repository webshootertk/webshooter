#!/usr/local/bin/python
import os
import subprocess

os.system("rm *.pyc")
subprocess.call(["rm", "-rf", "completed_files/"])
subprocess.call(["rm", "-rf", "doc_files/"])
subprocess.call(["rm", "-rf", "extracted_files/"])
subprocess.call(["rm", "-rf", "html_dirty_files/"])
subprocess.call(["rm", "-rf", "html_files/"])
subprocess.call(["rm", "-rf", "image_files/"])
subprocess.call(["rm", "-rf", "pdf_files/"])
#subprocess.call(["rm", "-rf", "whole_site/"])
