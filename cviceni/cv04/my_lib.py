# By Pytel, mothspaws
import os
import numpy as np
import matplotlib.pyplot as plt

def clear():
    """ Clear console """
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    #os.system('cls' if os.name == 'nt' else 'clear')

def intenzity_corecton(img, etalon) -> np.ndarray:
    """ Corect image intenzity
    
    Args:
        img : image to corect
        etalon : etalon image
        
    Returns:
        img : corected image
    """
    return img/etalon

def plot_imgs(imgs, titles, rows : int = 1, cmaps=None, cbars=None, figsize=(8,6), window_name="Graph"):
    """ Plot images
    
    Args:
        imgs : list of images
        titles : list of titles
        rows : number of rows
        cmap : color map
        figsize : size of figure
        window_name : name of window
    """
    plt.figure(window_name, figsize=figsize)
    #plt.rcParams["figure.figsize"] = figsize
    n = len(imgs)
    cols = int(np.ceil(n/rows))
    for i in range(n):
        img = imgs[i]
        plt.subplot(rows, cols, i+1)
        plt.imshow(img) 
        plt.title(titles[i])
        if cmaps != None and cmaps[i] != None:
            plt.set_cmap(cmaps[i])
        if cbars != None and cbars[i]:
            plt.colorbar(fraction=0.046, pad=0.04)
    plt.show()
    plt.waitforbuttonpress()

def fftshift(fft) -> np.ndarray:
    # np.fft.fftshift
    Y = fft.shape[0]
    X = fft.shape[1]
    ret = np.zeros([Y,X], dtype=complex)
    for y in range(Y):
        for x in range(X):
            ret[y][x] = fft[y][x]
    for y in range(Y):
        for x in range(X):
            ret[y][x] = fft[(y+Y//2)%Y][(x+X//2)%X]
    return ret

# amplitudové spektrum
def amp_spec(fft) -> np.ndarray:
    """ Calculate amplitude spectrum of image
    
    Args:
        fft : image to calculate amplitude spectrum
        
    Returns:
        amp_spec : amplitude spectrum of image
    """
    return np.log(np.abs(fft))

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
    
    Args:
        img : image to ekvalise
        q0 : start value
        p0 : start value
        qk : end value
    
    Returns:
        ekvalised : ekvalised image
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