__author__ = 'lidl'
import cv2

temfile='/Users/lidl/temfile.jpg'
img = cv2.imread('/Users/lidl/Desktop/tt/4-1632_2242.jpg')
crop_img = img[800:850, 80:150]
cv2.imshow("cropped", crop_img)
cv2.imwrite(temfile,crop_img);
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
