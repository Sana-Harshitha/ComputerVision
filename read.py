import cv2 as cv

profile=cv.imread('images/profile.jpg')


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.imshow("User", rescaleFrame(profile,0.5))
cv.waitKey(0)