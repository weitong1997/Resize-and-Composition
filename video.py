# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:25:12 2019

@author: ailee
"""

# import shutil
# import os
import cv2
import numpy as np
from imutils import paths

green_img_path = "green"
rb_img_path = "rb"


fps = 60   #视频帧率
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
videoWriter = cv2.VideoWriter('rb60_1080.avi', fourcc=fourcc, fps=fps, frameSize=(1920,1080))   #(1360,480)为视频大小

for i in range(1, 5342):
    img = cv2.imread(".\\" + rb_img_path + "\\" + str(i) + "_rb.png")
    # img = cv2.resize()
    img = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("img", img)
    cv2.waitKey(2)
    videoWriter.write(img)
        
videoWriter.release()
cv2.destroyAllWindows()


fps = 60   #视频帧率
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
videoWriter = cv2.VideoWriter('green60_1080.avi', fourcc=fourcc, fps=fps, frameSize=(1920,1080))   #(1360,480)为视频大小

for i in range(1, 5342):
    img = cv2.imread(".\\" + green_img_path + "\\" + str(i) + "_green.png")
    # img = cv2.resize()
    img = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_LINEAR)
    # cv2.imshow("img", img)
    # cv2.waitKey(2)
    print(".\\" + green_img_path + "\\" + str(i) + "_green.png")
    videoWriter.write(img)
        
videoWriter.release()
cv2.destroyAllWindows()
