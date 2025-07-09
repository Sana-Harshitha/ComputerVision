from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

frame = cv2.imread("../images/cat_vs_dog.jpg")
results = model.predict(source=frame, save=False, verbose=False)
r = results[0]

# Print the mapping of class indices to names
print("Class names dictionary:")
print(r.names)


# This gives you the class indices of only the detected objects
detected_class_ids = r.boxes.cls.cpu().numpy().astype(int)

# For example, you might get: [0, 15]
print("Detected class IDs:", detected_class_ids)

# Convert class IDs to names
detected_class_names = [r.names[cid] for cid in detected_class_ids]
print("Detected class names:", detected_class_names)
