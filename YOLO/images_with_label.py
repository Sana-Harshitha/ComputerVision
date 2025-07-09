from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

frame = cv2.imread("../images/cat_vs_dog.jpg")
results = model.predict(source=frame, save=False, verbose=False)
r = results[0]

# The original input image (as a numpy array)
print("Original image shape:", r.orig_img.shape)

# Original height and width
print("Original shape attribute:", r.orig_shape)
print("Probs attribute:", r.probs)

# Create an annotated image with boxes and labels drawn
annotated_img = r.plot()

# Show the annotated image
cv2.imshow("YOLOv8 Detections", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
