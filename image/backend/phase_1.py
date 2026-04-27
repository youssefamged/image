import cv2

# image = cv2.imread("2-2-car-transparent.png", 0)


def segmentation(image):
    algorithm = cv2.THRESH_BINARY

    threshold, output = cv2.threshold(image, 0, 255, algorithm + cv2.THRESH_OTSU)
    if image is None:
        return "no image found"

    return threshold, output

    # print("Best threshold =", threshold)

    # cv2.imshow("Original", image)
    # cv2.imshow("Output", result)


#  cv2.waitKey(0)
#  cv2.destroyAllWindows()