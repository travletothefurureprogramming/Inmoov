import cv2
from ultralytics import YOLO

model = YOLO("yolov8m.pt")

def find_object(cls_name):
    cap = cv2.VideoCapture(0)
    
    x_center, y_center, pixel_w = None, None, None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame")
            break
        
        results = model(frame, verbose=False)
        result = results[0]

        found_target = False
        for box in result.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            if class_name == cls_name:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x_center = int((x1 + x2) / 2)
                y_center = int((y1 + y2) / 2)
                pixel_w = int(x2 - x1)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (x_center, y_center), 4, (0, 0, 255), -1)
                found_target = True
                break  
            
        cv2.imshow("Mark's Vision Tracker", frame)
        
        if found_target:
            cap.release()
            cv2.destroyAllWindows()
            return x_center, y_center, pixel_w

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None, None, None