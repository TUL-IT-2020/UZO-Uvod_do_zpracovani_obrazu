# By Pytel

import cv2
import numpy as np

def intenzity_corecton(img, etalon) -> np.ndarray:
    """ Corect image intenzity
    
    Args:
        img : image to corect
        etalon : etalon image
        
    Returns:
        img : corected image
    """
    return img/etalon


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

def convolution(img, kernel):
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