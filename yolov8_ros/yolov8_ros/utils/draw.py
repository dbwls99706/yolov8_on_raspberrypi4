import cv2
import torch
import numpy as np

from ultralytics.engine.results import Results

def box(img, detection_output, class_list, colors) :    
    out_image = img 

    for run_output in detection_output :
        label, con, box = run_output        

        box_color = colors[int(label.item())]
        label = class_list[int(label.item())]
        
        first_half_box = (int(box[0].item()),int(box[1].item()))
        second_half_box = (int(box[2].item()),int(box[3].item()))
        cv2.rectangle(out_image, first_half_box, second_half_box, box_color, 2)
        
        text_print = '{label} {con:.2f}'.format(label = label, con = con.item())
        text_location = (int(box[0]), int(box[1] - 10 ))
        
        labelSize, baseLine = cv2.getTextSize(text_print, cv2.FONT_HERSHEY_SIMPLEX, 1, 1) 
        
        cv2.rectangle(out_image 
                        , (int(box[0]), int(box[1] - labelSize[1] - 10 ))
                        , (int(box[0])+labelSize[0], int(box[1] + baseLine-10))
                        , box_color , cv2.FILLED)        
        
        cv2.putText(out_image, text_print ,text_location
                    , cv2.FONT_HERSHEY_SIMPLEX , 1
                    , (255, 255, 255), 2, cv2.LINE_AA)

    return out_image

