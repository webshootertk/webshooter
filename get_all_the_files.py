#!bin/python
import subprocess

subprocess.call("/Users/harris112/Projects/aims/zpull.sh", shell=True)
subprocess.call("/Users/harris112/Projects/cf-convention/zpull.sh", shell=True)
subprocess.call("/Users/harris112/Projects/esgf/zpull.sh", shell=True)
subprocess.call("/Users/harris112/Projects/mattben/zpull.sh", shell=True)
subprocess.call("/Users/harris112/Projects/pcmdi/zpull.sh", shell=True)
subprocess.call("/Users/harris112/Projects/uv-cdat/zpull.sh", shell=True)
print "Done"
