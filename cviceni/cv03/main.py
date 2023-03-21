# By Pytel, mothspaws

"""
Vytvořte program (funkci) pro rotaci obrázku o libovolný úhel.
Použijte např. soubor cv03_robot.bmp. 
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from graphic import *

DEBUG = True

def calculate_shape(image, angle : float = 0) -> tuple():
    rows, cols, _ = image.shape
    #for coord in [(0, 0), (0, cols), (rows, 0), (rows, cols)]:
    #return (int(x_max), int(y_max))
    coord = (rows, cols)
    x, y = transform_coords(coord, generate_rotation_matrix((0, 0), angle))
    dim = max(abs(y), abs(x))
    return (int(dim), int(dim))

def calculate_translation(image, angle : float = 0) -> tuple():
    image_new_shape = calculate_shape(image, angle)
    rows, cols, _ = image.shape
    x = image_new_shape[0] - rows
    y = image_new_shape[1] - cols
    return (int(-x//2), int(-y//2))

def center_image(old_image_shape, new_image_shape) -> tuple():
    x = (new_image_shape[0] - old_image_shape[0])
    y = new_image_shape[1] - old_image_shape[1]
    return (int(x//2), int(y//2)) 

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

    plt.waitforbuttonpress()

def rotate_image(image, degrees : float = 0):
    # Plot
    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Original")

    plt.subplot(1, 3, 2)
    # project
    rows, cols, _ = image.shape
    center = (rows//2, cols//2)
    dst = np.zeros((rows, cols, 3), np.uint8)
    rotation_matrix = generate_rotation_matrix(center, degrees)
    dst = project_pixels(image, rotation_matrix, dst)
    plt.imshow(dst)
    plt.title("Projected")

    plt.subplot(1, 3, 3)
    # reshaped
    move = calculate_translation(image, degrees)
    movement_matrix = generate_translation_matrix(move)
    rotation_and_shift = (rotation_matrix@movement_matrix)

    if DEBUG:
        rows, cols = calculate_shape(image, degrees)
        print("degrees:", degrees)
        print("rows:", rows, "cols:", cols)
        print("rotation_matrix:\n", rotation_matrix)
        print("movement_matrix:\n", movement_matrix)
        print("rotation_and_shift:\n", rotation_and_shift)
        print()

    dst = warpAffine(image, rotation_and_shift, calculate_shape(image, degrees))
    plt.imshow(dst)
    plt.title("Reshaped")

    plt.show()
    plt.waitforbuttonpress()
    plt.close()    

def rotate_image_cv2(image, angle : float = 0):
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

    # 0, 90, 180, 270, 360
    rotate_image(img_rgb, 34)
    rotate_image(img_rgb, 120)
    rotate_image(img_rgb, 220)
    rotate_image(img_rgb, 285)

