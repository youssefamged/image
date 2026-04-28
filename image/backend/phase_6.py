def change_red_color(image, intensity):
    res = image.copy()
    res[:, :, 2] = intensity
    return res


def swap_red_to_green(image):
    res = image.copy()
    res[:, :, 1] = image[:, :, 2].copy()
    res[:, :, 2] = image[:, :, 1].copy()
    return res


def eliminate_red_channel(image):
    res = image.copy()
    res[:, :, 2] = 0
    return res