import cv2 as cv

capture =cv.VideoCapture("images/cat_video.mp4")

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video",rescaleFrame(frame,0.20))
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)