from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt') 

# Create a VideoCapture object
cap = cv2.VideoCapture("../images/cricket.mp4")

# Loop through each frame
while True:
    success, frame = cap.read()  # Read one frame

    if not success:
        break  # Exit loop if video is finished
    # Resize frame to half its original size

    scaled_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
    # cv2.imshow('Video Frame', scaled_frame)
    results = model.predict(source=scaled_frame, save=False,verbose=False)

    # Draw boxes manually
    annotated_frame = results[0].plot()  # draws boxes and labels

    cv2.imshow('YOLOv8 Video Detection', annotated_frame)

    if cv2.waitKey(100) == 27:  # ESC key to quit
        break

cap.release()
cv2.destroyAllWindows()
