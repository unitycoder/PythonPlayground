# https://docs.python.org/2/library/gzip.html

import os
import gzip
import shutil

currentPath = os.getcwd()+"\\"

print "GZipping-a-hoy"

# note include original file extension to output, otherwise its just "output"
with open(currentPath+'test\\img.jpg', 'rb') as f_in, gzip.open(currentPath+'output.png.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
    
print "Yay!"
