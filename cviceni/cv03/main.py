# By Pytel

"""
Vytvořte program (funkci) pro rotaci obrázku o libovolný úhel.
Použijte např. soubor cv03_robot.bmp. 
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from graphic import *

def project_image(image, M):
    """ Project image
    """
    # Plot
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original")

    plt.subplot(1, 2, 2)
    # project
    rows, cols, _ = image.shape
    dst = np.zeros((rows, cols, 3), np.uint8)
    dst = project_pixels(image, M, dst)
    plt.imshow(dst)
    plt.title("Projected")

    plt.show()

    plt.waitforbuttonpress()

def rotate_image(image, angle):
    """ Rotate image
    """
    # Plot
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original")

    plt.subplot(1, 2, 2)
    # rotate
    rows, cols, _ = image.shape
    center = (cols/2, rows/2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    print("Rows:", rows, "cols:", cols)
    print(M)
    dst = cv2.warpAffine(image, M, (cols, rows))
    plt.imshow(dst)
    plt.title("Rotated")

    plt.show()

    plt.waitforbuttonpress()

img_file = "cv03_robot.bmp"

if __name__ == "__main__":
    plt.ion()
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    elif os.name == 'posix':
        clear = lambda: os.system('clear')
    clear()
    plt.close('all')

    img = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    rows, cols, _ = img_rgb.shape
    center = (rows, 0)

    project_image(
        img_rgb, 
        generate_rotation_matrix(center, 45)
    )
    #rotate_image(img_file, 45)

