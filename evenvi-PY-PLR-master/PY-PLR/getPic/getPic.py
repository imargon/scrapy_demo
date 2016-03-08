from SimpleCV import Camera, Display, Image
import time, glob, os
import config

def captureImage():
    images_path = os.getcwd() + config.tmp_img_path
    image_path = os.path.join(images_path,"original.jpg")
    disp = Display(config.disp_size)
    cam = Camera(config.camera_no,{"width":640, "height":480})
    im = cam.getImage()
    im.save(image_path)
    return image_path

def imgDiff(threshold):

    cam = Camera(config.camera_no,{"width":640, "height":480})
    img = cam.getImage()
    screensize = img.width * img.height

    min_blob_size = 0.10 * screensize
    max_blob_size = 0.80 * screensize

    blobs = img.findBlobs(minsize=min_blob_size, maxsize=max_blob_size)

    print blobs

    if blobs:
        avgcolor = np.mean(blobs[-1].meanColor())
        if avgcolor > threshold:
            image_path = captureImage()

        if os.path.isfile(image_path):
            return 1
        else:
            return 0
def grayImg(image):
    gray = image.grayscale().binarize()
captureImage()
#imgDiff(150)
