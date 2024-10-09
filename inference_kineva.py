# KINEVA INFERENCE DEMO 08.10.2024
# REBOTNIX GmbH, all rights reserved.

from rb_engine.detect import Detector
import cv2
import numpy as np

# Generate a fixed color for each class and store them
def assign_colors_to_classes(classes):
    colors = {}
    for class_name in classes:
        # Generate a unique color for each class
        random_color = np.random.randint(0, 255, size=(3,))
        colors[class_name] = (int(random_color[0]), int(random_color[1]), int(random_color[2]))  # Convert to BGR tuple
    return colors

#initialize Detector
detector = Detector

#load model from file
detect = detector(
   weight_file="./model/kineva_person_head.best.pth",
   conf_thres=0.25,
   nms_thres=0.55,
   input_size=[640,640],
   fuse=False,
   fp16=False,
   use_decoder=False
)

#get class names
class_names = detect.class_names

#generate colors for class names
class_colors = assign_colors_to_classes(class_names)

#load images
img = cv2.imread("demos/d12.jpg")

# do detection
results = detect([img], False)

# draw rectangles on image
for res in results:
    if res is not None:
        for *xywh, obj, conf, cate in res:
            x1 = int(xywh[0])
            y1 = int(xywh[1])
            x2 = int(xywh[2])
            y2 = int(xywh[3])
            acc = float(obj * conf)
            catname = class_names[int(cate)]
            cv2.rectangle(img, (x1, y1), (x2, y2), class_colors[catname], 2)
            # Add the label above the rectangle
            label_position = (x1, y1 - 10)  # Slightly above the rectangle
            label_size = cv2.getTextSize(catname, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            # Coordinates of the background box
            box_top_left = (label_position[0] - 5, label_position[1] - label_size[1] - 5)
            box_bottom_right = (label_position[0] + label_size[0] + 5, label_position[1] + 5)
            cv2.rectangle(img, box_top_left, box_bottom_right, class_colors[catname], thickness=cv2.FILLED)
            cv2.putText(img, catname, label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), thickness=2)


#write image
cv2.imwrite("demos/result.jpg", img)
