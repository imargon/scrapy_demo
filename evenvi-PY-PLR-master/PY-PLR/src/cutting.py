__author__ = 'Evenvi'
from SimpleCV import Image, Display, Color, DrawingLayer
import numpy as np
import Image as LibImage
#import os, Image

def cuteImg(pack_blob_zoom,pack_blob_size):
    oriImg = Image("./img/original.jpg")
    cropImg = oriImg.crop(pack_blob_zoom[0]*2,pack_blob_zoom[1]*2.05,pack_blob_size[0]*0.85,pack_blob_size[1]*0.58,centered=True)
    cropImg.save("./img/dest5.jpg")
    #chiCropImg = cropImg.crop(0,0,cropImg.width*0.25, cropImg.height*2,centered=True)
    #chiCropImg.save("./img/chiPlate.jpg")
    #engCropImg = cropImg.crop(cropImg.width*0.22 ,0,cropImg.width*0.75, cropImg.height*2, centered=False)


    #engCropImg.show()
    #chiCropImg.show()
    #cropImg.show()

def getPoint(im, end=False):
    pixels = im.load()
    w, h = im.size
    range_w = end and range(w-1, 0, -1) or range(w)
    for x in range_w:
        for y in range(h):
            if pixels[x, y] == 0:
                return end and x + 1 or x

def getVerticalProjection(imPath):
    im = LibImage.open(imPath)
    # Obtained by vertical projection, return to the projection of data
    pixels = im.load()
    w, h = im.size
    start_x = getPoint(im)
    end_x = getPoint(im, end=True)
    graph = [0] * (end_x - start_x)
    for x in range(start_x, end_x):
        for y in range(h):
            pixel = pixels[x, y]
            if pixel == 0: # this list has character
                graph[x - start_x] += 1

    return start_x, end_x, graph

def showVerticalProjection(graph):
    # Display the vertical projection
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

def cut(start_x, end_x, graph, im):
    chars = [start_x]
    for i, v in enumerate(graph):
        if v !=0:
            if graph[i - 1] == 0:
                chars.append(i + start_x)
        elif graph[i - 1] !=0:
            chars.append(i + start_x)
    chars.append(end_x)

    result = list()
    for i in range(len(chars) - 1):
        result.append((chars[i], chars[i + 1] - 1))
    result = [v for (i, v) in enumerate(result) if not i%2] # Removal trough zero

    w, h = im.size
    chars = list()
    for char_start_x, char_end_x  in result:
        chars.append(im.crop((char_start_x, 0, char_end_x, h)))

    # Cut longitudinally and then transversely cut:
    result = list()
    for char in chars:
        w, h = char.size
        pixels = char.load()
        try:
            for y in range(h):
                for x in range(w):
                    if pixels[x, y] == 0:
                        start_y = y
                        raise
        except:
            pass
        try:
            for y in range(h-1, -1, -1):
                for x in range(w):
                    if pixels[x, y] == 0:
                        end_y = y
                        raise
        except:
            pass
        result.append(char.crop((0, start_y, w, end_y)))
    return result