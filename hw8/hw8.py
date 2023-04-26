import cv2
import numpy as np

def OtsuThreshold(img):
    img = img.copy()
    h, w = img.shape
    n = h * w
    oneD = img.ravel()
    hist = np.zeros(256)
    m = 0
    for i in oneD:  hist[i] += 1

    btAll = 0
    for i in range(256):
        btAll += hist[i] / n
        m += i * hist[i] / n

    at = 0
    mat = 0
    record = [0, 0]
    for t in range(256):
        at += hist[t] / n
        bt = btAll - at
        if at == 0 or bt == 0:    continue
        mat += t * hist[t] / n
        tmp = (mat - m * at) ** 2 / (at * bt)
        record = max(record, [tmp, t])
    img[img >= record[1]] = 255
    img[img < record[1]] = 0
    return img

if __name__ == '__main__':
    imgpath = input("Please Enter the input image path:")
    img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
    OtsuImg = OtsuThreshold(img)
    cv2.imshow('Input', img)
    cv2.imshow('OtsuImg', OtsuImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
