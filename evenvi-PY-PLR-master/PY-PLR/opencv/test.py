import cv,sys
capture = cv.CaptureFromCAM(1) # from webcam
frame  = cv.QueryFrame(capture)
newvideo = 'Videos/%d_%d_%d_%d_%d_%d.avi' % (localtime()[0],localtime()[1],localtime()[2],localtime()[3],localtime()[4],localtime()[5])
video = cv.CreateVideoWriter(newvideo, cv.CV_FOURCC('D','I','V','X'), 30, cv.GetSize(frame), 1)

while(1):
    frame  = cv.QueryFrame(capture)
cv.WriteFrame(video, frame)
key = cv.WaitKey( int((1/30.)*1000)+1 )

video = cv.CreateVideoWriter(newvideo, cv.CV_FOURCC('D','I','V','X'), 30, cv.GetSize(frame), 1)
if not video :
    print "Error in creating video writer"
    sys.exit(1)

video = cv.CreateVideoWriter(newvideo, cv.CV_FOURCC('F','L','V','1'), 30, cv.GetSize(frame), 1)