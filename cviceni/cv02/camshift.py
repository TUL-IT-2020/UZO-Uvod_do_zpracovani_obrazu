# By Pytel

import numpy as np
import cv2

def img2hue_histogram(img):
    """ Convert 
    """
    # RGB to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = hsv[:,:,0]

    # Histogram
    hist, b = np.histogram(hue, bins=256, range=(0, 256))

    # normalize histogram
    hist = hist / np.max(hist)

    return hist

def get_center_of_picture(picture):
    """ Get center of picture
    """
    pixel_sum = np.sum(picture)

    weight_x = 0
    weight_y = 0
    for x in range(picture.shape[1]):
        for y in range(picture.shape[0]):
            weight_x += picture[y, x] * x
            weight_y += picture[y, x] * y  
    
    x_center = weight_x / pixel_sum
    y_center = weight_y / pixel_sum 
    return x_center, y_center

class CamShift():
    def __init__(self, pattern_file) -> None:
        patern_bgr = cv2.imread(pattern_file)
        y, x, z = patern_bgr.shape
        self.x_size = x
        self.y_size = y

        self.pattern_hue_hist = img2hue_histogram(patern_bgr)

    def next_positon(self, next_img) -> tuple():
        hsv = cv2.cvtColor(next_img, cv2.COLOR_BGR2HSV)
        hue = hsv[:,:,0]
        hist, b = np.histogram(hue, 256, (0, 256))

        # img projection
        hue_projection = self.pattern_hue_hist[hue]

        # get center of hue projection
        x_center, y_center = get_center_of_picture(hue_projection)

        x1 = int(x_center - self.x_size/2)
        y1 = int(y_center - self.y_size/2)
        x2 = int(x_center + self.x_size/2)
        y2 = int(y_center + self.y_size/2)

        return ((x1, y1), (x2, y2))

    