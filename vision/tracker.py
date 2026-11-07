import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)

model = YOLO("yolov8m.pt")

def find_object(cls_name):
    ret, frame = cap.read()
    if not ret:
        return "Error"
        

    results = model(frame)

    result = results[0]

    for box in result.boxes:
        cls_id = int(box.cls[0])

        class_name = model.names[cls_id]

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        x_center = int((x1 + x2) / 2)
        y_center = int((y1 + y2) / 2)
        pixel_w = int(x2 - x1)

        if class_name == cls_name:
            print("I find it")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            cv2.circle(frame, (x_center, y_center), 4, (0, 0, 255), -1)

            return x_center, y_center, pixel_w

    cv2.imshow("Mark's Vision Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        return

cap.release()
cv2.destroyAllWindows()