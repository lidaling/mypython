#decoding:utf-8
#!/usr/bin/env python
'''
mouse_and_match.py [-i path | --input path: default ./]

Demonstrate using a mouse to interact with an image:
 Read in the images in a directory one by one
 Allow the user to select parts of an image with a mouse
 When they let go of the mouse, it correlates (using matchTemplate) that patch with the image.
 ESC to exit
'''
import numpy as np
from math import *
import sys
import os
import glob
import argparse
import cv2 as cv

drag_start = None#全局变量取方块鼠标拖拽时使用
sel = (0,0,0,0)#全局变量 长方形左上颌右下定点坐标存储

def onmouse(event, x, y, flags, param):#鼠标事件响应函数
    global drag_start, sel
    if event == cv.EVENT_LBUTTONDOWN:#左键按下时记录当前初始坐标，并初始化矩形sel
        drag_start = x, y
        sel = 0,0,0,0
    elif event == cv.EVENT_LBUTTONUP:#鼠标左键叹弹起时响应
        if sel[2] > sel[0] and sel[3] > sel[1]:#判断右下角坐标是否大于左上角
            patch = gray[sel[1]:sel[3],sel[0]:sel[2]]#取矩形区域内像素作为patch图像
            result = cv.matchTemplate(gray,patch,cv.TM_CCOEFF_NORMED)#返回遍历后匹配值矩阵，这里选择归一化相关系数匹配
            result = np.abs(result)**3
            val, result = cv.threshold(result, 0.01, 0, cv.THRESH_TOZERO)#将低于0。01的值赋值为0
            result8 = cv.normalize(result,None,0,255,cv.NORM_MINMAX,cv.CV_8U)#将result转化到0-255区间
            cv.imshow("result", result8)
        drag_start = None
    elif drag_start:
        #print flags
        if flags & cv.EVENT_FLAG_LBUTTON:#取当前坐标与初始坐标较小的为矩形坐标左上，较大的为右下
            minpos = min(drag_start[0], x), min(drag_start[1], y)
            maxpos = max(drag_start[0], x), max(drag_start[1], y)
            sel = minpos[0], minpos[1], maxpos[0], maxpos[1]
            img = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
            cv.rectangle(img, (sel[0], sel[1]), (sel[2], sel[3]), (0,255,255), 1)
            cv.imshow("gray", img)
        else:
            print "selection is complete"
            drag_start = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Demonstrate mouse interaction with images')
    #命令行输入参数 mouse_and_match.py -i 输入图像路径  默认为E:/imagetest
    parser.add_argument("-i","--input", default='E:/imagetest', help="Input directory.")
    args = parser.parse_args()
    path = args.input#获取图像路径参数
    print(path)

    cv.namedWindow("gray",1)
    cv.setMouseCallback("gray", onmouse)
    '''Loop through all the images in the directory'''
    for infile in glob.glob( os.path.join(path, '*.*') ):#遍历文件夹下的图片文件
        ext = os.path.splitext(infile)[1][1:] #get the filename extenstion
        if ext == "png" or ext == "jpg" or ext == "bmp" or ext == "tiff" or ext == "pbm":
            print infile

            img=cv.imread(infile,1)
            if img == None:
                continue
            sel = (0,0,0,0)
            drag_start = None
            gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imshow("gray",gray)
            if (cv.waitKey() & 255) == 27:
                break
    cv.destroyAllWindows()
