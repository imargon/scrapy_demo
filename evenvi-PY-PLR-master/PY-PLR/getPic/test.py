__author__ = 'Evenvi'

from SimpleCV import Camera
cam = Camera()
while True:
    cam.getImage().grayscale().binarize().show()
    #cam.getImage().show()