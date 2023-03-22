import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

def colorEqualizeHist(source, gray, grayhist):
    source = source * (grayhist / gray)
    source = np.clip(source, 0, 255)
    source = source.astype(np.uint8)
    return source

def drawHis(img):
    color = ('b','g','r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0, 256])
        plt.plot(histr, color = col)
        plt.xlim([0, 256])
    plt.show()

if __name__ == '__main__':
    imgpath = input("Please Enter the input image path:")
    img = cv2.imread(imgpath, cv2.IMREAD_COLOR)

    sizePar = 1
    cv2.namedWindow("Input",0)
    cv2.resizeWindow("Input", img.shape[1] // sizePar, img.shape[0] // sizePar)
    cv2.imshow('Input', img)

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histEqImg = cv2.equalizeHist(grayImg)
    grayImg3 = np.stack((grayImg,)*3, axis=-1)
    histEqImg3 = np.stack((histEqImg,)*3, axis=-1)
    colorHistEqImg = colorEqualizeHist(img.copy(), grayImg3, histEqImg3)

    cv2.namedWindow("gray",0)
    cv2.resizeWindow("gray", grayImg3.shape[1] // sizePar, grayImg3.shape[0] // sizePar)    
    cv2.imshow('gray', grayImg)
    
    cv2.namedWindow("histEq",0)
    cv2.resizeWindow("histEq", histEqImg.shape[1] // sizePar, histEqImg.shape[0] // sizePar)        
    cv2.imshow('histEq', histEqImg)
    
    cv2.namedWindow("colorHistEqImg",0)
    cv2.resizeWindow("colorHistEqImg", colorHistEqImg.shape[1] // sizePar, colorHistEqImg.shape[0] // sizePar)    
    cv2.imshow('colorHistEqImg', colorHistEqImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    drawHis(img)
    drawHis(colorHistEqImg)
