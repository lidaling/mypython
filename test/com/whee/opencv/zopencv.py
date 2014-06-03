import cv2

class tmatch:
    __dimg=''
    __timg=''
    def __init__(self,psrc,tsrc):
        self.__dimg=cv2.imread(psrc)
        self.__timg=cv2.imread(tsrc)

        self.__cimg = self.__dimg[0:700, 0:1200]
        self.__dimg=self.__cimg;
        self.__matchvalue=eval('cv2.TM_CCOEFF');

    def getposition(self):
        result = cv2.matchTemplate(self.__dimg,self.__timg,self.__matchvalue)
        cv2.normalize(result,result,0,255,cv2.NORM_MINMAX)
        mini,maxi,(mx,my),(Mx,My) = cv2.minMaxLoc(result)
        if self.__matchvalue in [0,1]:
            MPx,MPy = mx,my
        else:
            MPx,MPy = Mx,My
        return MPx,MPy
