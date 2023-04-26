# By Pytel

import numpy as np
from enum import Enum, auto

from my_libs.img.functional import *

class MorphologyOperation(Enum):
    GRAY_ERODE = auto()
    GRAY_DILATE = auto()
    GRAY_OPEN = auto()
    GRAY_CLOSE = auto()
    GRAY_TOP_HAT = auto()

def gray_erode_1D(img, kernel):
    pass

def gray_dilate_1D(img, kernel):
    pass

def gray_erode(img, kernel):
    out = np.zeros(img.shape, dtype=np.uint8)
    for i_x in range(img.shape[0]):
        for i_y in range(img.shape[1]):
            if img[i_x, i_y] == 0:
                continue
            min_val = 255
            for k_x in range(kernel.shape[0]):
                for k_y in range(kernel.shape[1]):
                    if kernel[k_x, k_y] == 0:
                        continue
                    x = i_x + k_x - kernel.shape[0] // 2
                    y = i_y + k_y - kernel.shape[1] // 2
                    if not valid_coord(x, y, img):
                        continue
                    if img[x, y] < min_val:
                        min_val = img[x, y]
            out[i_x, i_y] = min_val
    return out

def gray_dilate(img, kernel):
    out = np.zeros(img.shape, dtype=np.uint8)
    for i_x in range(img.shape[0]):
        for i_y in range(img.shape[1]):
            if img[i_x, i_y] == 255:
                continue
            max_val = 0
            for k_x in range(kernel.shape[0]):
                for k_y in range(kernel.shape[1]):
                    if kernel[k_x, k_y] == 0:
                        continue
                    x = i_x + k_x - kernel.shape[0] // 2
                    y = i_y + k_y - kernel.shape[1] // 2
                    if not valid_coord(x, y, img):
                        continue
                    if img[x, y] > max_val:
                        max_val = img[x, y]
            out[i_x, i_y] = max_val
    return out

def gray_open(img, kernel):
    eroded = gray_erode(img, kernel)
    dilarated = gray_dilate(eroded, kernel)
    return dilarated

def gray_close(img, kernel):
    dilarated = gray_dilate(img, kernel)
    eroded = gray_erode(dilarated, kernel)
    return eroded

def morphology(img, operation : MorphologyOperation, kernel):
    if operation == MorphologyOperation.GRAY_ERODE:
        return gray_erode(img, kernel)
    elif operation == MorphologyOperation.GRAY_DILATE:
        return gray_dilate(img, kernel)
    elif operation == MorphologyOperation.GRAY_OPEN:
        return gray_open(img, kernel)
    elif operation == MorphologyOperation.GRAY_CLOSE:
        return gray_close(img, kernel)
    elif operation == MorphologyOperation.GRAY_TOP_HAT:
        opened = gray_open(img, kernel)
        closed = gray_close(img, kernel)
        from processing import plot_imgs
        plot_imgs(
            [img, opened, closed], 
            ["Original", "Opened", "Closed"],
            1, ["gray", "gray", "gray"]
        )
        out = np.zeros(img.shape, dtype=np.uint8)
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                delta = int(closed[x, y]) - int(opened[x, y])
                if delta < 0:
                    out[x, y] = 0
                elif delta > 255:
                    out[x, y] = 255
                else:
                    out[x, y] = delta
        # return img - gray_open(img, kernel)
        return out.astype(np.uint8)
    else:
        raise Exception("Unknown operation")
