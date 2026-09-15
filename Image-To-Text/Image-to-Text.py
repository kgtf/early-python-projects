'''
Basic Algorithm:

    Ask for image
    Make copy of image
    Turn image to black and white (strictly black and white no gray and stuff see if even good)
    Get resolution of image to get rows and columns
    Turn BW image to list of pixel by pixel
    Create text file
    If pixel white: nothing | if pixel black: Place 0 in text file (change char as needed)
    Go through for entire row then new line character for next line in text file
    Return text file
    Delete old image
'''
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import math

root = tk.Tk()
root.withdraw()

origImgPath = filedialog.askopenfilename()

#open new image and convert BW
BWimage = Image.open(origImgPath, 'r')
BWimage = BWimage.convert('1')

#get resolution of image
wid, hgt = BWimage.size
width = int(wid)
height = int(hgt)

#if downscaling is needed of image
downscale = input("Do you want to downscale this image? (y/n):")
downscale = downscale.lower()
if downscale == 'y':
    factor = input("By what factor? Enter a number:")
    factor = int(factor)
    #downscale image and change width and height accordingly
    width = math.floor(width/factor)
    height = math.floor(height/factor)
    BWimage.thumbnail((width,height))
    width, height = BWimage.size
    
#get list of pixel colors
pixellist = list(BWimage.getdata())


#create text file
# write 0 if black pixel and space if white pixel
# to create new image
textimage = open('imagetext.txt', 'w')
for currHeight in range(height):
    for currWidth in range(width):
        pixel = pixellist[currHeight*width + currWidth]
        if pixel == 0:
            textimage.write(' ')
        elif pixel == 255:
            textimage.write('W')
    textimage.write('\n')

#close text file
textimage.close()
