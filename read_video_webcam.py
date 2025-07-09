import cv2

cap = cv2.VideoCapture(0)  # 0 for default webcam

while True:
    success, frame = cap.read()
    if not success:
        break

    # Resize frame to half its original size
    scaled_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    cv2.imshow('Webcam', scaled_frame)

    if cv2.waitKey(100) == 27:  # ESC key to quit
        break

cap.release()
cv2.destroyAllWindows()
