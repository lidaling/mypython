#!/usr/bin/env python
# coding: utf-8
import cv2
import uuid

def match(matchvalue):
    img2 = img.copy()

    result = cv2.matchTemplate(img,template,matchvalue)

    cv2.normalize(result,result,0,255,cv2.NORM_MINMAX)

    mini,maxi,(mx,my),(Mx,My) = cv2.minMaxLoc(result)    # We find minimum and maximum value locations in result

    print('mini:'+str(mini)+';maxi:'+str(maxi));
    print('mx:'+str(mx)+';my:'+str(my));
    print('Mx:'+str(Mx)+';My:'+str(My));


    if matchvalue in [0,1]: # For SQDIFF and SQDIFF_NORMED, the best matches are lower values.
        MPx,MPy = mx,my
    else:                   # Other cases, best matches are higher values.
        MPx,MPy = Mx,My

    print("forward:"+str(MPx)+","+str(MPy))
    # Normed methods give better results, ie matchvalue = [1,3,5], others sometimes shows errors
    cv2.rectangle(img2, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    cv2.imshow('input',img2)
    cv2.imshow('output',result)


#tmpitem='/tmp/'+str(uuid.uuid4())+'.jpg'
#tmpfile='/tmp/'+str(uuid.uuid4())+'.png'
#print('tmpitem:'+tmpitem+'|tmpfile:'+tmpfile)

img = cv2.imread('/Users/lidl/Desktop/tt/4-1658_2272.jpg')
template = cv2.imread('/Users/lidl/Desktop/tt/template.jpg')


#crop_img = img[0:900, 0:1600]
#template=img[200:400,100:300]
#cv2.imshow("cropped", crop_img)
#img=crop_img;

#img= cv2.imread(tmpitem)

#OpenCV定义的结构元素
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

#template= cv2.dilate(template,kernel);
#cv2.imwrite(tmpfile,template);
#template = cv2.imread(tmpfile)

trows,tcols = template.shape[:2]    # template rows and cols

cv2.namedWindow('input')

matchvalue = 0
max_Trackbar = 5

cv2.createTrackbar('method','input',matchvalue,max_Trackbar,match)

#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#for meth in methods:
#    method = eval(meth)
#    match(method)
# method=eval('cv2.TM_CCOEFF');
method=eval('cv2.TM_SQDIFF');
match(method)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
