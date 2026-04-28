import cv2
import numpy as np


def histogram_stretching(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_v, max_v = np.percentile(image, (2, 98))
    res = np.clip((image - min_v) * (255.0 / (max_v - min_v)), 0, 255).astype(np.uint8)

    return res


def histogram_equalization(image):
    #  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    res = cv2.equalizeHist(image)

    return res