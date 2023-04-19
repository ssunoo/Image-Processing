import cv2
import numpy as np
import math

def rotate(img, angle, flag):
    center = (img.shape[0] // 2, img.shape[1] // 2)
    transformM = cv2.getRotationMatrix2D(center, angle, 1.0)
    sin = math.sin(math.pi * angle / 180)
    cos = math.cos(math.pi * angle / 180)
    newH = int(img.shape[0] * cos + img.shape[1] * sin) 
    newW = int(img.shape[1] * cos + img.shape[0] * sin)
    transformM[0, 2] += newW // 2 - center[0]
    transformM[1, 2] += newH // 2 - center[1]
    rotatedImg = cv2.warpAffine(img, transformM, (newH, newW), flags=flag, borderValue=255)
    return rotatedImg

if __name__ == '__main__':
    img = np.zeros((512, 512), dtype=np.uint8)
    img[128:384, 128:384] = 255
    nearestImg = rotate(img, 30, cv2.INTER_NEAREST)
    bilinearImg = rotate(img, 30, cv2.INTER_LINEAR)

    cv2.imshow('Input', img)
    cv2.imshow('nighbor nearest', nearestImg)
    cv2.imshow('bilinearImg', bilinearImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()