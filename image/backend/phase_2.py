import cv2
import numpy as np


def edge_detect(image):
    if image is None:
        return None
    x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    result1 = np.sqrt(x**2 + y**2)
    result2 = np.uint8(np.clip(result1, 0, 255))
    return result2