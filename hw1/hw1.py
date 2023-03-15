import cv2
from tqdm import tqdm

def cvtGray(img):
    h, w, c = img.shape
    for row in tqdm(range(h)):
        for col in range(w):
            b, g, r = img[row, col]
            gray = b/3 + g/3 + r/3
            img[row, col] = (gray, gray, gray)
    return img


if __name__ == '__main__':
    imgpath = input("Please Enter the input image path:")
    img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    cv2.imshow('Source', img)
    cvtGray(img)
    cv2.imwrite('output.jpg', img)
    cv2.imshow('Gray', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
