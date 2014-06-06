#!/usr/bin/env python
# coding: utf-8
import sys
from zopencv import tmatch

def callback():
    print("in callback block...")

size=len(sys.argv)
if(size>3):
    psrc=sys.argv[1]
    tsrc=sys.argv[2]
    ystart=sys.argv[3]
    yend=sys.argv[4]
    xstart=sys.argv[5]
    xend=sys.argv[6]
    # 指定区域 ，python test.py /Users/lidl/Desktop/tt/4-1658_2272.jpg /Users/lidl/Desktop/tt/template.jpg 0 900 0 1200
    match=tmatch(psrc,tsrc,ystart,yend,xstart,xend)
else:
    psrc=sys.argv[1]
    tsrc=sys.argv[2]
    #不指定区域 匹配，整张图 ，python test.py /Users/lidl/Desktop/tt/4-1658_2272.jpg /Users/lidl/Desktop/tt/template.jpg
    match=tmatch(psrc,tsrc)

x,y=match.getposition();
print("x:"+str(x)+",y:"+str(y))