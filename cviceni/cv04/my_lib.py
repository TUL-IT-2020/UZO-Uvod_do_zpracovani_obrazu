# By Pytel
import numpy as np
import matplotlib.pyplot as plt

def intenzity_corecton(img, etalon) -> np.ndarray:
    """ Corect image intenzity
    get:
        img - image to corect
        etalon - etalon image
    return:
        img - corected image
    """
    return img/etalon

def plot_imgs(imgs, titles, rows : int = 1, cmap=None):
    """ Plot images
    get:
        imgs - list of images
        titles - list of titles
        rows - number of rows
        cmap - color map
    """
    n = len(imgs)
    cols = int(np.ceil(n/rows))
    if cmap != None:
        plt.set_cmap(cmap)
    for i in range(n):
        img = imgs[i]
        plt.subplot(rows, cols, i+1)
        plt.imshow(img) 
        plt.title(titles[i])
    plt.show()
    plt.waitforbuttonpress()

def histogram(img) -> np.ndarray:
    """ Calculate histogram of image
    get:
        img - image to calculate histogram
    return:
        hist - histogram of image
    """
    Y = img.shape[0]
    X = img.shape[1]
    hist = np.zeros([256,1])
    for y in range(Y):
        for x in range(X):
            hist[img[y][x]] +=1
    return hist

def sum_range(array, start=0, stop=0):
    return np.sum(array[start:stop])

def sumed(array) -> np.ndarray:
    ret = np.zeros(array.shape[0])
    sumed = 0
    for i in range(array.shape[0]):
        sumed += array[i]
        ret[i] = sumed
    return ret 

# TODO: use P0
def ekvalise(img, q0 = 0, p0 = 0, qk = 255) -> np.ndarray:
    """ Ekvalise image
    get:
        img - image to ekvalise
        q0 - start value
        p0 - start value
        qk - end value
    return:
        ekvalised - ekvalised image
    """
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