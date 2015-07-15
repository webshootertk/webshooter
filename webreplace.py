import tempfile
import os
import shutil
import yaml

# Replaces all occurrances of pattern with subst in file_path
# from http://stackoverflow.com/a/39110/392225
def replace(file_path, pattern, subst):
# Create temp file
  fh, abs_path = tempfile.mkstemp()
  new_file = open(abs_path,'w')
  old_file = open(file_path)
  for line in old_file:
    new_file.write(line.replace(pattern, subst))
# Close temp file
  new_file.close()
  os.close(fh)
  old_file.close()
# Remove original file
  os.remove(file_path)
# Move new file
  shutil.move(abs_path, file_path)
