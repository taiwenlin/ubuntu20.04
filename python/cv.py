import cv2
import numpy as np
# img = cv2.imread('/home/lintaiwen/Downloads/888.jpg')

# cv2.namedWindow('new', cv2.WINDOW_FREERATIO)
# cv2.imshow('new', img)
#cv2.waitKey(0)

# while(1):
#     key=cv2.waitKey(1)
#     if key&0xFF==ord('q'):
#         cv2.imwrite('/home/lintaiwen/Downloads/999.jpg',img)
#         break

def cv2_base():
    grp = cv2.imread('/home/lintaiwen/Downloads/888.jpg',cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('new', cv2.WINDOW_FREERATIO)
    cv2.imshow('new', grp)
    while(1):
        keyM=cv2.waitKey(1)
        if keyM&0xFF==ord('m') or keyM&0xFF==27:
            cv2.imwrite('/home/lintaiwen/Downloads/grp.jpg',grp)
            break
def split_channels(img):
    (B, G, R) = cv2.split(img)
    return B, G, R
def convert_format(B, G ,R):
    gray = cv2.cvtColor((B,G,R), cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor((B,G,R), cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor((B,G,R), cv2.COLOR_BGR2RGB)
    return gray, hsv, rgb
def show_img(img,delay_time):
    cv2.namedWindow('new', cv2.WINDOW_FREERATIO)
    cv2.imshow('new', img)
    cv2.waitKey(delay_time)


def filter(img, s):
    if(s=='Gauss'):
        img=cv2.GaussianBlur(img,(3,3),0)
    if(s=='median'):
        img=cv2.medianBlur(img,5 )
    if(s=='bilateral'):
        img=cv2.bilateralFilter(img, 51, 10, 10)
    return img

def do_canny(img):
    canny = cv2.Canny(img, 50, 150)
    return canny

if __name__=='__main__':
    org = cv2.imread('/home/lintaiwen/Downloads/888.jpg')

    # show_img(h,5000)
    # new=filter(org,'Gauss')
    # show_img(new,3000)
    # cv2.imwrite('/home/lintaiwen/Downloads/888_Gauss.jpg',new)
    # new=filter(org,'median')
    # show_img(new,3000)
    # cv2.imwrite('/home/lintaiwen/Downloads/888_median.jpg',new)
    # new=filter(org,'bilateral')
    # show_img(new,3000)
    # cv2.imwrite('/home/lintaiwen/Downloads/888_bilateral.jpg',new)
    new=filter(org,'Gauss')
    new=do_canny(new)
    # kernel=np.ones((3,3),np.uint8)
    # new = cv2.erode(new, kernel, 1)
    kernel=np.ones((27,27),np.uint8)
    new=cv2.dilate(new,kernel,1)
    show_img(new,3000)
    cv2.imwrite('/home/lintaiwen/Downloads/888new.jpg',new)