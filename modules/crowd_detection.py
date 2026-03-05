import cv2
import torch
import numpy as np
from tracker import Tracker
from config import camera, model, tracker, area, crowd_count
import time

OVERCROWD_THRESHOLD = 30
overcrowding_alert = False


crowd_count = 0
# Add this reset function to reset the crowd count
def reset_crowd_count():
    global crowd_count
    crowd_count = 0


# Function to get the latest crowd count
def get_crowd_count():
    global crowd_count
    return crowd_count
# Define a function to handle crowd frame generation with frame skipping and optimization
def generate_crowd_frame():
    global crowd_count,weapon_detected
    frame_skip = 3  # Process every 3rd frame to reduce load
    frame_counter = 0

    while True:
        success, frame = camera.read()
        if not success:
            break

        # Skip frames to reduce processing load
        frame_counter += 1
        if frame_counter % frame_skip != 0:
            continue  # Skip this frame

        # Resize the frame (optional: reduce resolution further if needed)
        frame = cv2.resize(frame, (640, 320))
        cv2.polylines(frame, [np.array(area, np.int32)], True, (0, 255, 0), 3)

        results = model(frame)
        list = []

        for index, row in results.pandas().xyxy[0].iterrows():
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            obj_name = str(row['name'])
            if obj_name == 'person':
                list.append([x1, y1, x2, y2])
        boxes_id = tracker.update(list)
        crowd_count = len(boxes_id)
        global overcrowding_alert
        if crowd_count > OVERCROWD_THRESHOLD:
            overcrowding_alert = True
        else:
            overcrowding_alert = False

        if overcrowding_alert:
            cv2.putText(frame,
                "OVER CROWDING ALERT!",
                (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                3)

        # Encode frame to JPEG and yield as multipart stream
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def get_overcrowding_status():
    global overcrowding_alert
    return overcrowding_alert