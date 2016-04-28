# Converts invidual cubemap face images into single image row
# output image can be then used as Cubemap inside unity
# more info: http://docs.unity3d.com/Manual/class-Cubemap.html
# NOTE: image filenames must contains directions

import os
from PIL import Image

print "\n-=[ IMAGES2CUBEMAP ]=-\n"

# settings
# TODO check if exists
currentPath = os.getcwd()+"\\"
inputFolder = currentPath+"images\\"
outputFolder = currentPath+"output\\"

print "Reading image files from: %s" % inputFolder

# get list of files
files = []
for file in os.listdir(inputFolder):
    if file.endswith(".jpg") or file.endswith(".png"):
        #print(file)
        files.append(inputFolder+file)
        if len(files)>6:
            print "ERROR: Too many images files in input folder - reading only first 6 images"
            break

# sort into +x(right) -x(left) +y(top) -y(bottom) +z(front) -z(back)

sortedList = [None]*6
for img in files:
    if "right" in img:
        sortedList[0] = img
    if "left" in img:
        sortedList[1] = img
    if "top" in img:
        sortedList[2] = img
    if "bottom" in img:
        sortedList[3] = img
    if "front" in img:
        sortedList[4] = img
    if "back" in img:
        sortedList[5] = img

# TODO: check if all images were founded

#if len(sortedList) is not len(files):
#    print "ERROR: Filenames are missing directions (right,left,top,bottom,front,back)"
#    sys.exit()


# load images
images = []
for img in sortedList:
    #print img   
    images.append(Image.open(img))
 
# create new bitmap
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
new_im = Image.new('RGB', (total_width, max_height))

# paste all images to the new bitmap
x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

# save
new_im.save(outputFolder+'output.png')

print "Finished!"
