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

def calculate_shape(image, angle):
    rows, cols, _ = image.shape
    angle = np.deg2rad(angle)
    cos = np.cos(angle)
    sin = np.sin(angle)
    x = cols * cos + rows * sin
    y = cols * sin + rows * cos
    return (int(x), int(y))

def calculate_translation(image, angle):
    image_new_shape = calculate_shape(image, angle)
    rows, cols, _ = image.shape
    x = image_new_shape[0] - rows
    y = image_new_shape[1] - cols
    x = (image_new_shape[0] - rows)//2
    y = 0
    return (int(x), int(y))

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

def rotate_image(image, degrees):
    # Plot
    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Original")

    plt.subplot(1, 3, 2)
    # project
    rows, cols, _ = image.shape
    dst = np.zeros((rows, cols, 3), np.uint8)
    rotation_matrix = generate_rotation_matrix(center, degrees)
    dst = project_pixels(image, rotation_matrix, dst)
    plt.imshow(dst)
    plt.title("Projected")

    plt.subplot(1, 3, 3)
    # reshaped
    rows, cols = calculate_shape(image, degrees)
    print(rows, "\n", cols)
    move = calculate_translation(image, degrees)
    movement_matrix = generate_translation_matrix(move)
    print("movement_matrix:\n", movement_matrix)
    print("rotation_matrix:\n", rotation_matrix)
    rot = (rotation_matrix@movement_matrix)
    print("rot:\n", rot)
    dst = np.zeros((rows, cols, 3), np.uint8)
    dst = project_pixels(image, rot, dst)
    plt.imshow(dst)
    plt.title("Reshaped")

    plt.show()
    plt.waitforbuttonpress()

def rotate_image_cv2(image, angle):
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

    # project_image(
    #     img_rgb, 
    #     generate_rotation_matrix(center, 45)
    # )

    rotate_image(img, 30)


