__author__ = 'Evenvi'

import os, sys, Image
import cv
import time

camera_port = 0

def getImage():
    filePath = os.getcwd()+"/img/original.jpg"
    print filePath
    cammra = cv.CaptureFromCAM(camera_port)
    im = cv.QueryFrame(cammra)
    cv.SaveImage(filePath, im)
    del(cammra)
    if os.path.isfile(filePath):
        return filePath
    else:
        return 0

"""
    img = cv.QueryFrame(capture)
    im_gray  = cv.CreateImage(cv.GetSize(img),cv.IPL_DEPTH_8U,1)
    cv.CvtColor(img,im_gray,cv.CV_RGB2GRAY)
"""

def grayImage(imagePath):
    #destImgPath = cv.CreateImage ((640,480), cv.IPL_DEPTH_8U, 3)
    destImgPath = os.getcwd()+"/img/dest1.jpg"
    img0 = cv.LoadImageM(imagePath,0)
    if not img0:
        print("could not load image")
        return
    #cv.CvtColor(img0, destImgPath, cv.CV_RGB2GRAY)
    cv.SaveImage(destImgPath,img0)
    return destImgPath

#im_gray: gray image path
def sobelImage(imGrayPath):
    destImgPath = os.getcwd()+"/img/dest2.jpg"
    im_gray = cv.LoadImageM(imGrayPath, cv.CV_LOAD_IMAGE_GRAYSCALE)
    dstSobel = cv.CreateMat(im_gray.height, im_gray.width, cv.CV_16S)
    cv.Sobel(im_gray,dstSobel, 1, 0)
    cv.SaveImage(destImgPath,dstSobel)
    return destImgPath


def sigma(im,i,debug =False):
    c0_p_num = sum(im.histogram()[:i+1])
    c1_p_num = sum(im.histogram()[i+1:])
    c0_g_sum = 0
    for j in range(1,i+1):
        c0_g_sum += j*im.histogram()[j]
        #end for j
    c1_g_sum = 0
    for j in range(i+1,255):
        c1_g_sum += j*im.histogram()[j]
        #end for j

    try:
        u0 = 1.0*c0_g_sum/c0_p_num
        u1 = 1.0*c1_g_sum/c1_p_num

        w0 = 1.0*c0_p_num/(c0_p_num+c1_p_num)
    except:

        return 0
    w1 = 1.0 - w0
    u = (u0-u1)**2
    new_sigma = w0 * w1 *u
    if debug:
        print "%d:\tw0=%f,w1=%f,new_sigma=%f" %(i,w0,w1,new_sigma)
    return new_sigma

def OtsuThreshold(im,debug = False):
    g_level = 0
    g_sigma = 0
    for i in range(1,255):
        new_sigma = sigma(im,i,debug)
        if g_sigma<new_sigma:
            g_sigma = new_sigma
        g_level = i
    #end for i
    return g_level, g_sigma

def thresholdImage(imSobelPath):
    destImgPath = os.getcwd()+"/img/dest3.jpg"
    print imSobelPath
    imSobel = cv.LoadImage(imSobelPath,cv.CV_LOAD_IMAGE_GRAYSCALE)
    dstImThreshold = cv.CreateImage((imSobel.width,imSobel.height),cv.IPL_DEPTH_8U,1)
    cv.Threshold(imSobel,dstImThreshold,100,255,cv.CV_THRESH_BINARY_INV)
    cv.SaveImage(destImgPath,dstImThreshold)

    return destImgPath
#geay image Corrode an Expand
def Change(image,flag = 0,num = 2):
    w = image.width
    h = image.height
    size = (w,h)
    iChange = cv.CreateImage(size,8,1)
    for i in range(h):
        for j in range(w):
            a = []
            for k in range(2*num+1):
                for l in range(2*num+1):
                    if -1<(i-num+k)<h and -1<(j-num+l)<w:
                        a.append(image[i-num+k,j-num+l])
            if flag == 0:
                k = max(a)
            else:
                k = min(a)
            iChange[i,j] = k
    return iChange

#geay image Corrode an Expand
def Two(image):
    w = image.width
    h = image.height
    size = (w,h)
    iTwo = cv.CreateImage(size,8,1)
    for i in range(h):
        for j in range(w):
            iTwo[i,j] = 0 if image[i,j] <220 else 255
    return iTwo

def  Corrode(image):
    w = image.width
    h = image.height
    size = (w,h)
    iCorrode = cv.CreateImage(size,8,1)
    kH = range(2)+range(h-2,h)
    kW = range(2)+range(w-2,w)
    for i in range(h):
        for j in range(w):
            if i in kH or j in kW:
                iCorrode[i,j] = 255
            elif image[i,j] == 255:
                iCorrode[i,j] = 255
            else:
                a = []
                for k in range(5):
                    for l in range(5):
                        a.append(image[i-2+k,j-2+l])
                if max(a) == 255:
                    iCorrode[i,j] = 255
                else:
                    iCorrode[i,j] = 0
    return iCorrode

def Expand(image):
    destImgPath = os.getcwd()+"/img/dest4.jpg"
    w = image.width
    h = image.height
    size = (w,h)
    iExpand = cv.CreateImage(size,8,1)
    for i in range(h):
        for j in range(w):
            iExpand[i,j] = 255
    for i in range(h):
        for j in range(w):
            if image[i,j] == 0:
                for k in range(5):
                    for l in range(5):
                        if -1<(i-2+k)<h and -1<(j-2+l)<w:
                            iExpand[i-2+k,j-2+l] = 0
    cv.SaveImage(destImgPath,iExpand)
    return iExpand

def opening(image):
    tmpImg = Corrode(image)
    openingImg = Expand(tmpImg)
    return openingImg

def closing(image):
    tmpImg = Expand(image)
    closingImg = Corrode(tmpImg)
    return closingImg


def findCounters():
    color_image = cv.QueryFrame(cv.CaptureFromCAM(0))
    grey_image = cv.CreateImage(cv.GetSize(cv.QueryFrame(cv.CaptureFromCAM(0))), cv.IPL_DEPTH_8U, 1)
    contour = cv.FindContours(grey_image, cv.CreateMemStorage(), cv.CV_RETR_TREE, cv.CV_CHAIN_APPROX_SIMPLE)
    points = []
    while contour:
        # Draw rectangles
        bound_rect = cv.BoundingRect(list(contour))
        contour = contour.h_next()

        pt1 = (bound_rect[0], bound_rect[1])
        pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
        points.append(pt1)
        points.append(pt2)
        cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 1)

    # Display frame to user
    cv.ShowImage("Target", color_image)
    return contour

imagePath = getImage()

imGrayPath = grayImage(imagePath)

imSobelPath = sobelImage(imGrayPath)

imThresholdPath = thresholdImage(imSobelPath)

im = Image.open(imSobelPath).convert("L")
debug = True
#threshold,max =  OtsuThreshold(im,debug)
#print threshold,max

imThreshold = cv.LoadImage(imThresholdPath,0)

iTwo = Expand(imThreshold)
iTwo2 = Corrode(iTwo)

iTwo3 = Expand(iTwo2)
iTwo4 = Corrode(iTwo3)

iTwo5 = Expand(iTwo4)
iTwo6 = Corrode(iTwo5)

iTwo7 = Expand(iTwo6)
iTwo8 = Corrode(iTwo7)

iTwo9 = Expand(iTwo8)
iTwo10 = Corrode(iTwo9)

iTwo11 = Expand(iTwo10)
iTwo12 = Expand(iTwo11)
iTwo13 = Expand(iTwo12)
iTwo14 = Expand(iTwo13)
iTwo15 = Expand(iTwo14)
iTwo16 = Expand(iTwo15)

#iTwo5 = closing(iTwo4)
#iTwo6 = opening(iTwo5)


#findCounters()

cv.ShowImage('iTwo',iTwo16)
#findCounters()

print  imThresholdPath
cv.WaitKey(0)