import cv2 as cv

profile=cv.imread('images/profile.jpg')

cv.imshow("User", profile)

cv.waitKey(0)