import cv2
import numpy as np
import cv

if __name__=='__main__':
    org = cv2.imread('/home/lintaiwen/Downloads/cup_lidX3.jpg',cv2.IMREAD_GRAYSCALE)
    cv.show_img(org,3000)
    new=cv.filter(org,'Gauss')
    new=cv.do_canny(new)
    cv.show_img(new,3000)
    kernel=np.ones((3,3),np.uint8)
    new=cv2.dilate(new,kernel,1)
    cv.show_img(new,3000)
    cv2.imwrite('/home/lintaiwen/Downloads/cup_lidX3new.jpg',new)