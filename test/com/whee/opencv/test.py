#!/usr/bin/env python
# coding: utf-8
import sys
from zopencv import tmatch

def callback():
    print("in callback block...")

size=len(sys.argv)
if(size>2):
    psrc=sys.argv[1]
    tsrc=sys.argv[2]
    ystart=sys.argv[3]
    yend=sys.argv[4]
    xstart=sys.argv[5]
    xend=sys.argv[6]
    match=tmatch(psrc,tsrc,ystart,yend,xstart,xend)
else:
    psrc=sys.argv[1]
    tsrc=sys.argv[2]
    match=tmatch(psrc,tsrc)

x,y=match.getposition();
print("x:"+str(x)+",y:"+str(y))