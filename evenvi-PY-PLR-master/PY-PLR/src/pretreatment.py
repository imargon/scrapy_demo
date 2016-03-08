"""
Capture and process images
author: Evenvi
time: 2013.4.20
"""
import os, sys, Image
import config
import cv

image = 0
element_shape = cv.CV_SHAPE_RECT

class PreTreatment:
    def __init__(self):
        self.name = []
        self.size = (640,480)

    def getImage(self,im):
        filePath = os.getcwd()+"/img/original.jpg"
        #print filePath
        #camera = cv.CaptureFromCAM(config.camera_port)
        #im = cv.QueryFrame(camera)
        cv.SaveImage(filePath, im)
        #del(camera)
        if os.path.isfile(filePath):
            return filePath
        else:
            return 0

    #binary
    def binary(self,f):
        img = Image.open(f)
        #img = img.convert('1')
        pixdata = img.load()
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        return img

    #convert to gray image
    def grayTr(self,image,array):
        w = image.width
        h = image.height
        size = (w,h)
        iGrayTr = cv.CreateImage(size,image.depth,1)
        for i in range(h):
            for j in range(w):
                idex = int(image[i,j])
                iGrayTr[i,j] = array[idex]
        return iGrayTr
    def slice(self):
        aSlice = [0]*256
        for i in range(256):
            if i>59 and i<121:
                aSlice[i] = 200
            else:
                aSlice[i] = 30
        return aSlice

    def sobelImage(self,imGrayPath):
        destImgPath = os.getcwd()+"/img/dest2.jpg"
        im_gray = cv.LoadImageM(imGrayPath, cv.CV_LOAD_IMAGE_GRAYSCALE)
        dstSobel = cv.CreateMat(im_gray.height, im_gray.width, cv.CV_16S)
        cv.Sobel(im_gray,dstSobel, 1, 0)
        cv.SaveImage(destImgPath,dstSobel)
        return destImgPath

    def sigma(self,im,i,debug =False):
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

    def OtsuThreshold(self,im,debug = False):
        g_level = 0
        g_sigma = 0
        for i in range(1,255):
            new_sigma = self.sigma(im,i,debug)
            if g_sigma<new_sigma:
                g_sigma = new_sigma
            g_level = i
            #end for i
        return g_level, g_sigma

    def thresholdImage(self,imSobelPath):
        destImgPath = os.getcwd()+"/img/dest3.jpg"
        #print imSobelPath
        imSobel = cv.LoadImage(imSobelPath,cv.CV_LOAD_IMAGE_GRAYSCALE)
        dstImThreshold = cv.CreateImage((imSobel.width,imSobel.height),cv.IPL_DEPTH_8U,1)
        cv.Threshold(imSobel,dstImThreshold,100,255,cv.CV_THRESH_BINARY_INV)
        cv.SaveImage(destImgPath,dstImThreshold)

        return destImgPath
        #geay image Corrode an Expand
    def Change(self,image,flag = 0,num = 2):
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
    def Two(self,image):
        w = image.width
        h = image.height
        size = (w,h)
        iTwo = cv.CreateImage(size,8,1)
        for i in range(h):
            for j in range(w):
                iTwo[i,j] = 0 if image[i,j] <220 else 255
        return iTwo

    def Opening(self, src,pos):
        element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
        dest = cv.CreateImage(self.size, 8, 3)
        image = cv.CreateImage(self.size,8, 3)
        cv.Erode(src, image, element, 1)
        cv.Dilate(image, dest, element, 1)
        return dest

    def Closing(self,src,pos):
        element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
        dest = cv.CreateImage(self.size, 8, 3)
        cv.Dilate(src, image, element, 1)
        cv.Erode(image, dest, element, 1)
        #cv.ShowImage("Opening & Closing", dest)
        return dest

    def Erosion(self,src,pos):
        element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
        dest = cv.CreateImage(self.size,8, 3)
        cv.Erode(src, dest, element, 1)
        #cv.ShowImage("Erosion & Dilation", dest)
        return dest

    def Dilation(self,src,pos):
        #src = cv.CreateImage(self.size, 8, 1)
        dest = cv.CreateImage(self.size, 8, 3)
        element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
        cv.Dilate(src, dest, element, 1)
        #cv.ShowImage("Erosion & Dilation", dest)
        return  dest


