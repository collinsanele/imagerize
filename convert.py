#!/usr/bin/env python
from cartoonizer import cartoonize
import cv2
import os
import time

in_dir = 'imgs/input'
out_dir = 'imgs/output'

if not os.path.exists(os.path.join(os.getcwd(), out_dir)):
	os.mkdir(out_dir)


for path, dirs,files in os.walk(os.path.join(os.getcwd(), in_dir)):
    for file in files:
        if file.endswith("jpg") or file.endswith("png"):
            image = cv2.imread(os.path.join(path, file))
            print('==============')
            print(image)
            start_time = time.time()
            #print(image)
            output = cartoonize(image)
            end_time = time.time()
            print("time: {0}s".format(end_time-start_time))
            name = os.path.basename(file)
            tmp = os.path.splitext(name)
            name = tmp[0]+"_cartoon" + tmp[1]
            name = os.path.join(out_dir, name)
            print("write to {0}".format(name))
            cv2.imwrite(name, output)