import cv2 as cv
import numpy as np 

blankImage=np.zeros((500,500,3),dtype='uint8') #uint8=>image datatype
# cv.imshow('blank_image',blankImage)

#paint the img a certain color

# blankImage[:]=0,0,255
# cv.imshow("Red",blankImage)
# blankImage[100:200,300:400]=0,255,0
# cv.imshow("Green",blankImage)

cv.rectangle(blankImage,(50,50),(250,250),(0,250,0),thickness=-1)
cv.imshow('Rectangle in image',blankImage)

cv.circle(blankImage,(250,250),40,(0,0,255),thickness=1)
cv.imshow('circle',blankImage)

cv.circle(blankImage,(300,400),40,(0,0,255),thickness=-1)
cv.imshow('circle',blankImage)

cv.putText(blankImage,"Hello",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow("Text",blankImage)
cv.waitKey(0)