__author__ = 'Evenvi'
import tesseract
import cv

#image = cv.LoadImage("./img/plateBinary.jpg",cv.CV_LOAD_IMAGE_GRAYSCALE)
image = cv.LoadImage("./img/plateBinary.jpg",cv.CV_LOAD_IMAGE_GRAYSCALE)
#chiImage = cv.LoadImage("./img/chiPlate.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE)

def recognize(image):
    api = tesseract.TessBaseAPI()
    api.Init(".","eng",tesseract.OEM_DEFAULT)
    api.SetPageSegMode(tesseract.PSM_AUTO)

    tesseract.SetCvImage(image, api)
    text = api.GetUTF8Text()
    conf = api.MeanTextConf()

    return text

def chiRecognize(image):
    api = tesseract.TessBaseAPI()
    api.Init(".","chi_sim",tesseract.OEM_DEFAULT)
    api.SetPageSegMode(tesseract.PSM_AUTO)

    tesseract.SetCvImage(image, api)
    text = api.GetUTF8Text()
    conf = api.MeanTextConf()

    return text

#print "Plate NO. is:"+recognize(image)
print "PlateCHI NO. is:"+chiRecognize(image)