# By Pytel

import cv2
import numpy as np


def img_to_g(img) -> np.ndarray:
    """ Convert image to g.

    Args:
        img: image to convert

    Return:
        g: g image
    
    #### Algorithm:
    g = (G*255)/(R+G+B)
    """
    #emps = float(1e-10)
    R = img[:,:,0].astype(float)
    G = img[:,:,1].astype(float)
    B = img[:,:,2].astype(float)
    g = (G*255)/(R+G+B)# + emps)
    return g.astype(np.uint8)

def segmentate(
        img, 
        threshold : np.uint8 = 100, 
        scale : np.uint8 = 255
    ) -> np.ndarray:
    """ Segmentate image by threshold.

    Args:
        img: image to segmentate
        threshold: threshold value
        scale: scale of weigths (0-1)*scale

    Return:
        img: image with 0 and 255
    """
    # img : 0-1
    img_segmented = img > threshold
    # img : 0-255 <= (0-1)*scale
    img_segmented = img_segmented * scale
    return img_segmented.astype(np.uint8)


def flood_fill(img, img_filled, x, y, object_number) -> bool:
    """ Flood fill algorithm.

    Args:
        img: image to fill
        img_filled: image with filled points 
        x: x coordinate of start point
        y: y coordinate of start point
        object_number: number of object

    Return:
        True if point is filled, False if not
    """

    # TODO: remove recursion !!!

    X, Y = img.shape
    # 1) check if point is in image
    if x < 0 or x >= X or y < 0 or y >= Y:
        return False
    # 2) check if point is not filled
    if img_filled[x][y] != 0:
        return False
    # 3) check if point is not background
    if img[x][y] == 255:
        return False
    # 4) fill point and call flood_fill for neighbours
    img_filled[x][y] = object_number
    for vector in [(0,1), (0,-1), (1,0), (-1,0)]:
        dx, dy = vector
        flood_fill(img, img_filled, x+dx, y+dy, object_number)
    return True

def color_objects(img : np.ndarray) -> tuple():
    """ Collor objects in image by separate numbers.

    Args:
        img: image to collor objects

    Return:
        img: image with collored objects
        object_number: number of objects

    #### Algorithm
    Maximal number of objects is 255.
    Img background value is 255.
    Collor background number is 0.
    """
    X, Y = img.shape
    objects = np.zeros([X, Y], dtype=np.uint8)
    object_number = 1
    for x in range(X):
        for y in range(Y):
            if img[x][y] == 255:
                continue
            elif flood_fill(img, objects, x, y, object_number):
                object_number += 1

    return objects, object_number

def histogram(img) -> np.ndarray:
    """ Calculate histogram of image
    
    Args:
        img : image to calculate histogram
        
    Returns:
        hist : histogram of image
    """
    Y = img.shape[0]
    X = img.shape[1]
    hist = np.zeros([256,1])
    for y in range(Y):
        for x in range(X):
            hist[img[y][x]] +=1
    return hist

def convolution(img, kernel : np.ndarray) -> np.ndarray:
    """ Implements 2D convolution 

    Args:
        img : image to convolute
        kernel : kernel to convolute

    Returns:
        new_img : convoluted image
    """
    X_img, Y_img = img.shape
    X_ker, Y_ker = kernel.shape
    
    img = cv2.copyMakeBorder(img, X_ker-1, X_ker-1, Y_ker-1, Y_ker-1, cv2.BORDER_CONSTANT, value=128)
    
    new_img = np.zeros((X_img, Y_img))
    for x in range(X_ker-1, X_img + X_ker-1):
        for y in range(Y_ker-1, Y_img + Y_ker-1):
            new_img[x-X_ker+1, y-Y_ker+1] = np.sum(np.multiply(img[x-X_ker+1:x+1, y-Y_ker+1:y+1], kernel))

    return new_img

def intenzity_corecton(img, etalon) -> np.ndarray:
    """ Corect image intenzity
    
    Args:
        img : image to corect
        etalon : etalon image
        
    Returns:
        img : corected image

    #### Algorithm:
    img = img / etalon
    """
    return (img/etalon).astype(np.uint8)

def normalize(img) -> np.ndarray:
    """ Normalize image to 0-255.

    Args:
        img: image to normalize
    
    Return:
        img: normalized image

    #### Algorithm:
    img = (img - min(img)) / (max(img) - min(img)) * 255
    """
    img_min = np.min(img)
    img_max = np.max(img)
    img = img - img_min
    img = img / (img_max - img_min)
    img = img * 255
    return img.astype(np.uint8)

# TODO: use P0
def ekvalise(img, q0 = 0, p0 = 0, qk = 255) -> np.ndarray:
    """ Ekvalise image
    
    Args:
        img : image to ekvalise
        q0 : start value
        p0 : start value
        qk : end value
    
    Returns:
        ekvalised : ekvalised image
    """
    def sumed(array) -> np.ndarray:
        ret = np.zeros(array.shape[0])
        sumed = 0
        for i in range(array.shape[0]):
            sumed += array[i]
            ret[i] = sumed
        return ret 

    Y = img.shape[0]
    X = img.shape[1]
    hist = histogram(img)
    #hist = np.histogram(img, bins=256)[0]
    sumed_values = sumed(hist)
    coef = (qk-q0)/(X*Y)
    ekvalised = np.zeros([Y,X])
    for y in range(Y):
        for x in range(X):
            ekvalised[y][x] = coef * sumed_values[img[y][x]]
    return ekvalised.astype('uint8')
