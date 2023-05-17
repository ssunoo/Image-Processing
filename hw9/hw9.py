import cv2
import numpy as np

def skeletonization(img):
    img = img.copy()
    size = np.size(img)
    skl = np.zeros(img.shape,np.uint8)
 
    img[img>127] = 255
    img[img<=127] = 0
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
    
    while( not done):
        eroded = cv2.erode(img,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(img,temp)
        skl = cv2.bitwise_or(skl,temp)
        img = eroded.copy()
    
        zeros = size - cv2.countNonZero(img)
        if zeros==size:
            done = True
    
    return skl

if __name__ == '__main__':
    imgpath = input("Please Enter the input image path:")
    img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
    skeleton = cv2.ximgproc.thinning(img)
    ske2 = skeletonization(img)
    cv2.imshow('Input', img)
    cv2.imshow('OpenCV function', skeleton)
    cv2.imshow('Lantuejoul’s  skeletonization method ', ske2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
