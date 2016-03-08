"""
Hough calculation of the image tilt angle
parameter:
    srcImg  : source image
    srcWidth: width of source image
    srcHeight: height of source image
return:
    true
    false

author:Evenvi

time:2013.4.21
"""
import cv
import math

def XWarp(image,angle):
    a = math.tan(angle*math.pi/180.0)
    W = image.width
    H = int(image.height+W*a)
    size = (W,H)
    iWarp = cv.CreateImage(size,image.depth,image.nChannels)
    for i in range(image.height):
        for j in range(image.width):
            x = int(i+j*a)
            iWarp[x,j] = image[i,j]
    return iWarp

def YWarp(image,angle):
    a = math.tan(angle*math.pi/180.0)
    H = image.height
    W = int(image.width+H*a)
    size = (W,H)
    iYWarp = cv.CreateImage(size,image.depth,image.nChannels)
    for i in range(image.height):
        for j in range(image.width):
            y = int((H-i)*a+j)
            iYWarp[i,y] = image[i,j]
    return iYWarp

def TYWarp(image,angle):
    a = math.sin(angle*math.pi/180.0)
    H = image.height
    W = int(image.width+H*a)
    size = (W,H)
    iTYWarp = cv.CreateImage(size,image.depth,image.nChannels)
    for i in range(image.height):
        for j in range(image.width):
            y = int((H-i)*a+j)
            iTYWarp[i,y] = image[i,j]
    return iTYWarp


image = cv.LoadImage('./img/dest5.jpg',1)
iWarp1 = XWarp(image,1)
iWarp2 = TYWarp(iWarp1,5)
iWarp3 = XWarp(iWarp2,25)
cv.ShowImage('image',image)
cv.ShowImage('1',iWarp1)
cv.ShowImage('2',iWarp2)
cv.ShowImage('3',iWarp3)
cv.WaitKey(0)






