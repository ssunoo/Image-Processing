import cv2
import numpy as np
from tqdm import tqdm

def ditheringL4(img):
    ditheringMatrix = np.array([[0, 56], 
                                [84, 28]])
    h, w, c = img.shape
    ditheringArray = np.zeros((h, w))
    walk = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    print('Generating dithering array...')
    for row in tqdm(range(0, h, 2)):
        for col in range(0, w, 2):
            for step in walk:
                try:
                    ditheringArray[row + step[0]][col + step[1]] = ditheringMatrix[step[0]][step[1]]
                except:
                    continue
    print('Dithering...')

    for row in tqdm(range(h)):
        for col in range(w):
            value = img[row][col][0] // 85
            if img[row][col][0] - 85 * value > ditheringArray[row][col]: 
                value += 1
            value *= 85
            img[row][col] = value, value, value
    return img

def ditheringL2(img):
    ditheringMatrix = np.array([[0, 128], 
                                [192, 64]])
    h, w, c = img.shape
    ditheringArray = np.zeros((h, w))
    walk = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    print('Generating dithering array...')
    for row in tqdm(range(0, h, 2)):
        for col in range(0, w, 2):
            for step in walk:
                try:
                    ditheringArray[row + step[0]][col + step[1]] = ditheringMatrix[step[0]][step[1]]
                except:
                    continue
    print('Dithering...')
    for row in tqdm(range(h)):
        for col in range(w):
            if img[row][col][0] > ditheringArray[row][col]:
                img[row][col] = 255, 255, 255
            else: 
                img[row][col] = 0, 0, 0
    return img


if __name__ == '__main__':
    imgpath = 'input.jpg'
    # imgpath = input("Please Enter the input image path:")
    img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    L2Out = ditheringL2(img.copy())
    L4Out = ditheringL4(img.copy())
    
    cv2.imshow('Source', img)
    cv2.imshow('Dithering matrix L2', L2Out)
    cv2.imshow('Dithering matrix L4', L4Out)

    cv2.imwrite('outputL2.jpg', L2Out)
    cv2.imwrite('outputL4.jpg', L4Out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

