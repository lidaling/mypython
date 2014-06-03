#!/usr/bin/env python
# coding: utf-8
import sys
from zopencv import tmatch

def callback():
    print("in callback block...")

psrc=sys.argv[1];
tsrc=sys.argv[2]
match=tmatch(psrc,tsrc)

x,y=match.getposition();
print("x:"+str(x)+",y:"+str(y))