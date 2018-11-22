#!/usr/bin/env python3

import cv2
#import numpy as np
from display import Display

W = 1920 // 2
H = 1080 // 2

d = Display(W=W, H=H)


def process_frame(img):
    print(img.shape)
    img = cv2.resize(img, (W, H))
    d.paint(img)


if __name__ == "__main__":

    #cap = cv2.VideoCapture("test.mp4")
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            process_frame(frame)
        else:
            break
