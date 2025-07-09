# import cv2 as cv

# capture =cv.VideoCapture("images/cat_video.mp4")

# def rescaleFrame(frame,scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions=(width,height)

#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video",rescaleFrame(frame,0.20))
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)

import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture("images/cat_video.mp4")

# Loop through each frame
while True:
    success, frame = cap.read()  # Read one frame

    if not success:
        break  # Exit loop if video is finished
    # Resize frame to half its original size

    scaled_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
    cv2.imshow('Video Frame', scaled_frame)

    if cv2.waitKey(100) == 27:  # ESC key to quit
        break

cap.release()
cv2.destroyAllWindows()
