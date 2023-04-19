import cv2
import numpy as np
import random
import math
import matplotlib.pyplot as plt

def Gaussian(img, sigma):
    img = img.copy()
    rlt = np.zeros_like(img, dtype=np.uint16)
    for row in range(0, img.shape[0], 2):
        for col in range(img.shape[1]):
            r = random.random()
            phi = random.random()
            z1 = sigma * math.cos(2 * math.pi * phi) * (-2 * math.log(r)) ** 0.5
            z2 = sigma * math.sin(2 * math.pi * phi) * (-2 * math.log(r)) ** 0.5
            try:
                rlt[row][col] = img[row][col] + z1
                rlt[row + 1][col] = img[row + 1][col] + z2
            except:
                pass
    rlt = np.clip(rlt, 0, 255)
    rlt = rlt.astype(np.uint8)
    return rlt

def showGrayImgHis(img):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()    

if __name__ == '__main__':
    img = np.zeros((512, 512), dtype=np.uint8)
    img[0:512, 0:512] = 100
    rltImg = Gaussian(img, 5.0)    
    cv2.imshow('Input', img)
    cv2.imshow('Gaussian', rltImg)
    showGrayImgHis(img)    
    showGrayImgHis(rltImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
