__author__ = 'Evenvi'
import cv

def Hist(image,color = cv.RGB(255,255,255)):
    a = [0]*256
    w = image.width
    h = image.height
    iHist = cv.CreateImage((256,256),8,3)
    for i in range(h):
        for j in range(w):
            iGray = int(image[i,j])
            a[iGray] = a[iGray] + 1
    S = max(a)
    for k in range(256):
        a[k] = a[k]*255/S
        x = (k,255)
        y = (k,255-a[k])
        cv.Line(iHist,x,y,color)
    return iHist

def GrayTr(image,array):
    w = image.width
    h = image.height
    size = (w,h)
    iGrayTr = cv.CreateImage(size,image.depth,1)
    for i in range(h):
        for j in range(w):
            idex = int(image[i,j])
            iGrayTr[i,j] = array[idex]
    return iGrayTr

def Invert():
    aInvert = [0]*256
    for i in range(256):
        aInvert[i] = 255 - i
    return aInvert

def thresholdImage(imSobel):

    imSobel = imSobel
    dstImThreshold = cv.CreateImage((imSobel.width,imSobel.height),cv.IPL_DEPTH_8U,1)
    cv.Threshold(imSobel,dstImThreshold,100,255,cv.CV_THRESH_BINARY_INV)

    return dstImThreshold

image = cv.LoadImage('./img/dest5.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)

iInvert = GrayTr(image,Invert())
iThresInvert =thresholdImage(iInvert)

cv.ShowImage('image',image)
cv.ShowImage('iInvert',iInvert)
cv.ShowImage('threshold',iThresInvert)


cv.ShowImage('iIHist',Hist(iInvert))

cv.WaitKey(0)