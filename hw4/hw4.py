import cv2
import numpy as np

def unSharpMasking(origin, strength, sigma, filter="median"):
    origin = origin.astype(np.int16)
    if filter == "median":
        blurImg = cv2.medianBlur(origin, sigma)
    elif filter == "average":
        blurImg = cv2.blur(origin, (sigma, sigma))
    else:
        return
    result = origin + strength * (origin - blurImg)
    result = np.clip(result, 0, 255)
    result = result.astype(np.uint8)
    return result

if __name__ == '__main__':
    imgpath = input("Please Enter the input image path:")
    img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    averageUnsharpMask = np.zeros_like(img)
    medianUnsharpMask = np.zeros_like(img)
    averageUnsharpMask = unSharpMasking(img, 3, 5, "average")
    medianUnsharpMask = unSharpMasking(img, 3, 5, "median")
    cv2.imshow('Input', img)
    cv2.imshow('average blur', averageUnsharpMask)
    cv2.imshow('median blur', medianUnsharpMask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()