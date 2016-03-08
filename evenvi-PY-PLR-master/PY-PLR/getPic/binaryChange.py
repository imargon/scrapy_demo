__author__ = 'Evenvi'
import cv

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
    return iExpand


image = cv.LoadImage('pic3.jpg',0)
iTwo = Two(image)
iCorrode = Corrode(iTwo)
iExpand = Expand(iTwo)

cv.ShowImage('image',image)
cv.ShowImage('iTwo',iTwo)
cv.ShowImage('iCorrode',iCorrode)
cv.ShowImage('iExpand',iExpand)
cv.WaitKey(0)
