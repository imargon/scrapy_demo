__author__ = 'Evenvi'
#! /usr/bin/env python
# coding: u8
import os, sys, Image,ImageFilter,ImageEnhance
import cv
import time

GRID_COLOR = (49, 36, 115)
BG_COLOR = (49, 36, 115)
ARC_COLOR = (104, 109, 106)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
def eraseGridAndArc(im):
    w, h = im.size
    pixels = im.load()
    for y in range(h):
        for x in range(w):
            pixel = pixels[x, y]
            if pixel == BG_COLOR or pixel == GRID_COLOR:
                im.putpixel((x, y), WHITE)
            elif pixel == ARC_COLOR:
                up = y > 0 and pixels[x, y-1] or None
                down = y < h-1 and pixels[x, y+1] or None
                up_down = up or down
                im.putpixel((x, y), up_down and up_down or WHITE)
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(255)
    im = im.convert('1')
    im.show()
    return im

def grayImage(imagePath):
    #destImgPath = cv.CreateImage ((640,480), cv.IPL_DEPTH_8U, 3)
    destImgPath = os.getcwd()+"/img/dest11.jpg"
    img0 = cv.LoadImageM(imagePath,0)
    if not img0:
        print("could not load image")
        return
        #cv.CvtColor(img0, destImgPath, cv.CV_RGB2GRAY)
    cv.SaveImage(destImgPath,img0)
    return destImgPath

def getPoint(im, end=False):
    pixels = im.load()
    w, h = im.size
    range_w = end and range(w-1, 0, -1) or range(w)
    for x in range_w:
        for y in range(h):
            if pixels[x, y] == 0:
                return end and x + 1 or x
def getVerticalProjection(im):
    pixels = im.load()
    w, h = im.size
    start_x = getPoint(im)
    end_x = getPoint(im, end=True)
    graph = [0] * (end_x - start_x)
    for x in range(start_x, end_x):
        for y in range(h):
            pixel = pixels[x, y]
            if pixel == 0:
                graph[x - start_x] += 1
    return start_x, end_x, graph
def showVerticalProjection(graph):
    w = len(graph)
    h = max(graph)
    img = Image.new('1', (w, h))
    for x in range(w):
        for y in range(h):
            if y <= graph[x]:
                img.putpixel((x, y), 255)
            else:
                break
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.show()

if __name__ == '__main__':
    im = Image.open('./img/dest5.png')
    #grayImagePath = grayImage(oriImgPath)

    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(6)
    im = im.convert('1')
    im = im.filter(ImageFilter.MedianFilter)

    im = eraseGridAndArc(im)
    dest11Img = Image.open(im)
    dest11Img = dest11Img.convert('1')
    #dest11Img = dest11Img.filter(ImageFilter.MedianFilter)

    dest11ImgPath = "./img/dest12.jpg"

    graph = getVerticalProjection(dest11Img)
    showVerticalProjection(graph)
    print graph






#cv.SaveImage(dest11ImgPath,dest11Img)
