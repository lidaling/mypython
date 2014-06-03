#!/usr/bin/env python
# coding: utf-8

import os
import cv2

def MatchingMethod(match_method):
    rows, cols = img.shape[:2]
    trows, tcols = templ.shape[:2]
    img_display = img.copy()
    mt = [cv2.TM_SQDIFF,
          cv2.TM_SQDIFF_NORMED,
          cv2.TM_CCORR,
          cv2.TM_CCORR_NORMED,
          cv2.TM_CCOEFF,
          cv2.TM_CCOEFF_NORMED]
    result = cv2.matchTemplate(img, templ, mt[match_method])
    print(result)
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
    if mt[match_method] == cv2.TM_SQDIFF or mt[match_method] == cv2.TM_SQDIFF_NORMED :
        matchloc = minloc
    else:
        matchloc = maxloc

    cv2.rectangle(img_display, matchloc, (matchloc[0] + trows, matchloc[1] + tcols), (0, 0, 0))
    cv2.rectangle(result, matchloc, (matchloc[0] + trows, matchloc[1] + tcols), (70, 100, 200))
    cv2.imshow(image_window, img_display)
    cv2.imshow(result_window, result)

if __name__ == '__main__':
    testpath = '/Users/lidl/Desktop/girl'
    #source = 'sys-pref.png'
    #tmpl = 'network-icon.png'
    source = 'form.png'
    tmpl = 'template.jpeg'
    global img
    img = cv2.imread(os.path.join(testpath, source))
    global templ
    templ = cv2.imread(os.path.join(testpath, tmpl))

    global image_window
    image_window = "Source Image"
    global result_window
    result_window = "Result window"
    global match_method
    match_method = 0

    max_Trackbar = 5

    trackbar_label = "sMethod: \n 0: TM SQDIFF \n 1: TM SQDIFF NORMED \n 2: TM CCORR \n 3: TM CCORR NORMED \n 4: TM COEFF \n 5: TM COEFF NORMED"

    cv2.namedWindow(image_window, cv2.CV_WINDOW_AUTOSIZE)
    cv2.namedWindow(result_window, cv2.CV_WINDOW_AUTOSIZE)
    cv2.createTrackbar(trackbar_label, image_window, match_method, max_Trackbar, MatchingMethod)
    MatchingMethod(match_method)
    cv2.waitKey(0)

