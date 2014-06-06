import cv2

class tmatch:
    def __init__(self,psrc,tsrc,ystart=0,yend=0,xstart=0,xend=0):
        self.__dimg=cv2.imread(psrc)
        self.__timg=cv2.imread(tsrc)

        trows,tcols = self.__dimg.shape[:2]
        if(ystart==0 and yend==0):
            yend=trows
        if(xstart==0 and xend==0):
            xend=tcols
        print(ystart,yend,xstart,xend)
        self.__cimg = self.__dimg[int(ystart):int(yend), int(xstart):int(xend)]
        self.__dimg=self.__cimg;
        # self.__matchvalue=eval('cv2.TM_CCOEFF');
        self.__matchvalue=eval('cv2.TM_SQDIFF');

        #cv2.imshow("cropped", self.__cimg)
        #if cv2.waitKey(0) == 27:
        #    cv2.destroyAllWindows()


    def getposition(self,callback=None):
        result=self.domatch();
        if callback != None:
            callback();
        return result;

    def domatch(self):
        result = cv2.matchTemplate(self.__dimg,self.__timg,self.__matchvalue)
        cv2.normalize(result,result,0,255,cv2.NORM_MINMAX)
        mini,maxi,(mx,my),(Mx,My) = cv2.minMaxLoc(result)


        if self.__matchvalue in [0,1]:
            MPx,MPy = mx,my
        else:
            MPx,MPy = Mx,My

        return MPx,MPy
