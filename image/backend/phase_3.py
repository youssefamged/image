import cv2
import numpy as np


def dilation(image):
    if image is None:
        return None
    threshold, binary = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    kernal = np.ones((3, 3), np.uint8)
    output = cv2.dilate(binary, kernal, iterations=2)
    return output, threshold


def erosion(image):
    if image is None:
        return None
    threshold, binary = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    kernal = np.ones((3, 3), np.uint8)
    output = cv2.erode(binary, kernal, iterations=2)

    return output, threshold


def opening(image):
    if image is None:
        return None
    threshold, binary = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    kernal = np.ones((3, 3), np.uint8)
    output = cv2.erode(binary, kernal, iterations=2)
    output = cv2.dilate(output, kernal, iterations=2)
    return output, threshold


def internal_boundary(image):
    if image is None:
        return None

    threshold, binary = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = np.ones((3, 3), np.uint8)

    erosion = cv2.erode(binary, kernel, iterations=1)  # orignal - erosion

    output = cv2.subtract(binary, erosion)

    return output, threshold


def external_boundary(image):
    if image is None:
        return None

    threshold, binary = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = np.ones((3, 3), np.uint8)

    dilation = cv2.dilate(binary, kernel, iterations=1)  # dilation - orignal

    output = cv2.subtract(dilation, binary)

    return output, threshold


def morphological_gradient(image):
    if image is None:
        return None

    threshold, binary = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = np.ones((3, 3), np.uint8)

    dilation = cv2.dilate(binary, kernel, iterations=1)
    erosion = cv2.erode(binary, kernel, iterations=1)

    output = cv2.subtract(dilation, erosion)

    return output, threshold
