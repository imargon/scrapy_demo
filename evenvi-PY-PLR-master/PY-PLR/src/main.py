__author__ = 'Evenvi'
#motion detection using opencv an simplecv
import cv
from SimpleCV import Image, Display, Color, DrawingLayer
import numpy as np
import pretreatment,cutting,plateProcess
import os, wx
import gui

class Target:
    def __init__(self):
        self.capture = cv.CaptureFromCAM(0)
        cv.NamedWindow("Target", 1)
        self.structing_element = np.ones((3,3), dtype=np.uint8)

    def run(self):
        # Capture first frame to get size
        frame = cv.QueryFrame(self.capture)
        frame_size = cv.GetSize(frame)
        grey_image = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
        moving_average = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_32F, 3)
        difference = None

        while True:
            # Capture frame from webcam
            color_image = cv.QueryFrame(self.capture)


            preImg = pretreatment.PreTreatment()
            imagePath = preImg.getImage(color_image)
            sobelImagePath = preImg.sobelImage(imagePath)
            thresholdImagePath = preImg.thresholdImage(sobelImagePath)
            print thresholdImagePath
            imThreshold = cv.LoadImage(thresholdImagePath,0)


            src = cv.LoadImage(thresholdImagePath, cv.CV_LOAD_IMAGE_COLOR)
            image = cv.CloneImage(src)
            dest = cv.CloneImage(src)

            #cv.ShowImage("texture", src)

            erDest = preImg.Erosion(src,6)
            opDest = preImg.Opening(erDest,6)
            erDest = preImg.Erosion(opDest,3)

            #save image
            cv.ShowImage("last result",erDest)
            filePath = os.getcwd()+"/img/dest4.jpg"
            cv.SaveImage(filePath,erDest)


            #img = cv.Convert(erDest,)

            img = Image("./img/dest4.jpg")
            blobs = img.binarize().findBlobs()
            pack_blobs = blobs.crop()
            pack_blob_size =  pack_blobs[-1].size()

            blobs.image = img
            print blobs.sortArea()[-1].area()
            blobArea = blobs.sortArea()[-1].area()
            nickels = blobs.filter((blobs.area() > blobArea-10) & (blobs.area() < blobArea+10))
            pack_blob_zoom = (nickels.center()[0][0]/2,nickels.center()[0][1]/2)

            debug = True
            color = (0,0,255)

            rect_start = (nickels.center()[0][0]-pack_blob_size[0]/2,nickels.center()[0][1]-pack_blob_size[1]/2)

            rect_end = (nickels.center()[0][0]+pack_blob_size[0]/2,nickels.center()[0][1]+pack_blob_size[1]/2)
            cv.Rectangle(color_image, rect_start, rect_end, color, 2, 0)

            cutting.cuteImg(pack_blob_zoom,pack_blob_size)

            # palte prccessing
            plateSrcPath = "./img/dest5.jpg"
            plateBinaryImg = plateProcess.binary(plateSrcPath)

            plateBinary = cv.LoadImage("./img/plateBinary.jpg", cv.CV_LOAD_IMAGE_COLOR)
            cv.ShowImage("Binary Plare",plateBinary)


            #start_x, end_x, graph = cutting.getVerticalProjection("./img/plateBinary.jpg")
            #chars = cutting.cut(start_x,end_x,plateBinary)


            # Display frame to user
            cv.ShowImage("Target", color_image)

            # Listen for ESC or ENTER key
            c = cv.WaitKey(7) % 0x100

            if c == 27 or c == 10:
                break

if __name__=="__main__":
    #app = wx.PySimpleApp()
    #frame = gui.MyFrame()
    #frame.Show(True)

    t = Target()
    t.run()

