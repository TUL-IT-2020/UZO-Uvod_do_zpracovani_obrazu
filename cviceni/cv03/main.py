# By Pytel

"""
Vytvořte program (funkci) pro rotaci obrázku o libovolný úhel.
Použijte např. soubor cv03_robot.bmp. 
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

def generate_rotation_matrix(center : tuple() = (0,0), angle: float = 0) -> np.array:
    """ Generate rotation matrix
    """
    angle = np.deg2rad(angle)
    cos = np.cos(angle)
    sin = np.sin(angle)
    x, y = center
    M = np.array([
        [cos, -sin, x*(1-cos)+y*sin],
        [sin, cos, y*(1-cos)-x*sin]]
    )
    return M

def transform_coords(point : tuple(), M : np.array) -> tuple():
    """ Project point
    """
    x, y = point
    vector = np.array([x, y, 1])
    vector = np.dot(M, vector)
    return (vector[0], vector[1])

def valid_point(coord : tuple(), shape : tuple()) -> bool:
    """ Validate point coordinates
    """
    x, y = coord
    X, Y, _ = shape
    if x < 0 or x >= X or y < 0 or y >= Y:
        return False
    return True

def project_pixels(source, M, destination) -> np.array:
    """ Project pixels
    get:
        source - source image
        M - inverse transformation matrix
        destination - blank destination image
    return:
        destination - transformed image
    """
    Y, X, _ = destination.shape
    for x in range(X):
        for y in range(Y):
            coord = transform_coords((x, y), M)
            y_orig = int(coord[1])
            x_orig = int(coord[0])
            if valid_point(coord, source.shape):
                destination[y, x] = source[y_orig, x_orig]
    return destination

def warpAffine(image, M, dsize):
    """ Warp affine
    """
    rows, cols, _ = dsize
    dst = np.zeros((rows, cols, 3), np.uint8)
    dst = project_pixels(image, M, dst)
    return dst

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
    center = (0, rows)

    project_image(
        img_rgb, 
        generate_rotation_matrix(center, -45)
    )
    #rotate_image(img_file, 45)

