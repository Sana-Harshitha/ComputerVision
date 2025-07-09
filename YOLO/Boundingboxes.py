from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture("../images/cat_video.mp4")

while True:
    success, frame = cap.read()
    if not success:
        break

    results = model.predict(source=frame, save=False, verbose=False)
    r = results[0]

    # Loop through all detected boxes
    for box in r.boxes:
        coords = box.xyxy[0].cpu().numpy().astype(int)  # [x1, y1, x2, y2]
        conf = float(box.conf[0])                      # Confidence score
        class_id = int(box.cls[0])                     # Class index
        label = r.names[class_id]                      # Class label name

        print(f"Detected [{label}] with confidence {conf:.2f} at {coords}")
        #it will print for every frame

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
