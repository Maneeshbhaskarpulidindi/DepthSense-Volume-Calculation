from realsense_camera import RealsenseCamera
from object_detection import ObjectDetection
import cv2
import numpy as np

# Create the Camera object 
camera = RealsenseCamera()

object_detection = ObjectDetection()

while True:
    # Get frame from realsense camera
    ret, color_image, depth_image = camera.get_frame_stream()
    height, width, _ = color_image.shape

    # Get the object detection
    bboxes, class_ids, scores = object_detection.detect(color_image)
    for bbox, class_id, score in zip(bboxes, class_ids, scores):
        x, y, x2, y2 = bbox
        color = object_detection.colors[class_id]
        cv2.rectangle(color_image, (x, y), (x2, y2), color, 2)

        # Display name
        class_name = object_detection.classes[class_id]
        cv2.putText(color_image, f"{class_name}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

        # Get center of the bbox
        cx, cy = (x + x2) // 2, (y + y2) // 2
        distance = camera.get_distance_point(depth_image, cx, cy)

        # Slicing the image
        bbox_depth = depth_image[y:y2, x:x2]
        max_depth = (np.max(bbox_depth))//100
        min_depth = (np.min(bbox_depth))//100

        # Calculate area in pixels
        area = ((x2 - x) * (y2 - y))//100

        # Calculate volume assuming depth is in centimeters and converting area to cm²
        volume = area * abs(max_depth - min_depth)
        # Draw circle
        cv2.circle(color_image, (cx, cy), 5, color, -1)
        cv2.putText(color_image, f"Area: {area} cm^2", (cx, cy + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
        #cv2.putText(color_image, f"Min Depth: {min_depth:.2f} cm", (cx, cy + 20),
         #           cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
        #cv2.putText(color_image, f"distance: {distance:.2f} cm", (cx, cy + 60),
         #           cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)                    
        cv2.putText(color_image, f"Volume: {volume:.2f} cc", (cx, cy + 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    # Show color image
    cv2.imshow("Color Image", color_image)
    #cv2.imshow("Depth Image", depth_image)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the camera
camera.release()
cv2.destroyAllWindows()
