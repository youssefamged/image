import cv2


def restore_sp_average(image):
    return cv2.blur(image, (5, 5))


def restore_sp_median(image):
    return cv2.medianBlur(image, 5)


def restore_sp_outlier(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)


def restore_gauss_averaging(image):
    blurred = cv2.blur(image, (5, 5))
    res = cv2.addWeighted(image, 0.5, blurred, 0.5, 0)
    return res


def restore_gauss_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)