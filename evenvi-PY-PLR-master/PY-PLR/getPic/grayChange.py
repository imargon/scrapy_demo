__author__ = 'Evenvi'

import cv

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


image = cv.LoadImage('lena.jpg',0)
iCorrode = Change(image)
iExpand = Change(image,1)
iOpen = Change(iCorrode,1)
iClose = Change(iExpand)
cv.ShowImage('image',image)
cv.ShowImage('iCorrode',iCorrode)
cv.ShowImage('iExpand',iExpand)
cv.ShowImage('iOpen',iOpen)
cv.ShowImage('iClose',iClose)
cv.WaitKey(0)
