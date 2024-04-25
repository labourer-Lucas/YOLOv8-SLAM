import cv2
from ultralytics import YOLO
import numpy as np
import torch
import os
source='rgb'
model = YOLO('yolov8n-seg.pt')
results = model.predict(source, save=True, classes=[0], show_labels=False,stream=True, show_boxes=False, show_conf=False, device='0')
for result in results:
    if len(result.boxes)==0:
        input_path = result.path  # Your input path string
        print(input_path)
        output_path = os.path.join(os.path.basename(input_path))
        print(output_path)
        print("no detections for" + output_path)
        cv2.imwrite(str('output/'+output_path), np.zeros((480, 640, 3), np.uint8))
    else : 
    # get array results
        masks = result.masks.data
        boxes = result.boxes.data
        clss = boxes[:, 5]
        # extract classes
        # get indices of results where class is 0 (people in COCO)
        people_indices = torch.where(clss == 0)
        # use these indices to extract the relevant masks
        people_masks = masks[people_indices]
        # scale for visualizing results
        people_mask = torch.any(people_masks, dim=0).int() * 255
        # save to file
        input_path = result.path  # Your input path string
        print(input_path)
        output_path = os.path.join(os.path.basename(input_path))
        print(output_path)
        cv2.imwrite(str('output/'+output_path), people_mask.cpu().numpy())
