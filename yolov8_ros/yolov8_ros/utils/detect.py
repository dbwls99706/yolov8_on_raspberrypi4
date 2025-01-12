import sys
import torch
import cv2
import random
import time
from ultralytics import YOLO
import utils.draw as draw
import RPi.GPIO as GPIO
import asyncio
import threading

GPIO.setwarnings(False)

def yolov8_detection(model, image, q):
    img_size = 256
    confidence = 0.5
    stream_buffer = True
    verb = False

    if q == 'int8':
        results = model.predict(image, imgsz=img_size, conf=confidence, verbose=verb, int8=True)
    else:
        results = model.predict(image, imgsz=img_size, conf=confidence, verbose=verb)

    result = results[0].cpu()

    box = result.boxes.xyxy.numpy()
    conf = result.boxes.conf.numpy()
    cls = result.boxes.cls.numpy().astype(int)

    return cls, conf, box

def detect_camera(model_path, q):
    model = YOLO(model_path, task='detect')

    label_map = model.names
    COLORS = [[0, 0, 255]] * len(label_map)

    GPIO.setmode(GPIO.BCM)
    output_pin = 23
    GPIO.setup(output_pin, GPIO.OUT)
    output_pin2 = 24
    GPIO.setup(output_pin2, GPIO.OUT)

    video_cap1 = cv2.VideoCapture(0)
    video_cap2 = cv2.VideoCapture(2)

    video_cap1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    video_cap2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    while True:
        ret1, frame1 = video_cap1.read()
        ret2, frame2 = video_cap2.read()

        if not ret1 or not ret2:
            break

        start = time.time()

        cls1, conf1, box1 = yolov8_detection(model, frame1, q)
        detection_output1 = list(zip(cls1, conf1, box1))

        cls2, conf2, box2 = yolov8_detection(model, frame2, q)
        detection_output2 = list(zip(cls2, conf2, box2))

        image_output1 = draw.box(frame1, detection_output1, label_map, COLORS)
        image_output2 = draw.box(frame2, detection_output2, label_map, COLORS)

        box_size_threshold = 20000
        if detection_output1:
            for x1, y1, x2, y2 in [box for _, _, box in detection_output1]:
                if (x2 - x1) * (y2 - y1) > box_size_threshold:
                    GPIO.output(output_pin, True)
            pin_state = GPIO.input(output_pin)
            print(f'Camera 1 - GPIO Pin State: {pin_state}')
        else:
            GPIO.output(output_pin, False)
            pin_state=GPIO.input(output_pin)
            print(f'Camera 1 - GPIO Pin State: {pin_state}')
        if detection_output2:
            for x1, y1, x2, y2 in [box for _, _, box in detection_output2]:
                if (x2 - x1) * (y2 - y1) > box_size_threshold:
                    GPIO.output(output_pin2, True)
            pin_state = GPIO.input(output_pin2)
            print(f'Camera 2 - GPIO Pin State: {pin_state}')
        else:
            GPIO.output(output_pin2, False)
            pin_state=GPIO.input(output_pin2)
            print(f'Camera 1 - GPIO Pin State: {pin_state}')
            

        end = time.time()

        cv2.imshow('Detection1', image_output1)
        cv2.imshow('Detection2', image_output2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_cap1.release()
    video_cap2.release()
    cv2.destroyAllWindows()
