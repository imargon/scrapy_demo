__author__ = 'Evenvi'
from SimpleCV import Image, Display, Color, DrawingLayer
import numpy as np
import time

img = Image("./img/dest4.jpg")
blobs = img.binarize().findBlobs()

pack_blobs = blobs.crop()
pack_blob_size =  pack_blobs[-1].size()

print type(pack_blob_size)
blobs.image = img
print blobs.sortArea()[-1].area()
blobArea = blobs.sortArea()[-1].area()
nickels = blobs.filter((blobs.area() > blobArea-10) & (blobs.area() < blobArea+10))


pack_blob_zoom = (nickels.center()[0][0]/2,nickels.center()[0][1]/2)


boxLayer = DrawingLayer((img.width,img.height))
boxLayer.rectangle(pack_blob_zoom,pack_blob_size,color=Color.RED)

img.addDrawingLayer(boxLayer)
img.show()

oriImg = Image("./img/original.jpg")
cropImg = oriImg.crop(pack_blob_zoom[0]*2,pack_blob_zoom[1]*2,pack_blob_size[0]*0.85,pack_blob_size[1]*0.68,centered=True)

cropImg.save("./img/dest5.jpg")

cropImg.show()

#nickels.show(width = 3)
time.sleep(3)