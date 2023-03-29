# By Pytel
"""
Z obrázků cv05_robotS.bmp a cv05_PSS.bmp odstraňte šum:  
a) pomocí metody prostého průměrování 
b) pomocí metody s rotující maskou 
c) pomocí mediánu 
 
Ke  všem  výsledkům  (a  původnímu  obrázku)  zobrazte  amplitudové 
spektrum a histogram.
"""

import sys
import cv2
sys.path.append('../')
from cv04.my_lib import *
from cv03.graphic import *

robot = "cv05_robotS.bmp"
PSS = "cv05_PSS.bmp"

def task_a(img, kernel_size = 3):
    img_bgr = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # get spectrum
    spectrum = np.fft.fftshift(np.fft.fft2(img_gray))

    # apply filters
    kernel = np.ones((kernel_size, kernel_size)) / kernel_size**2
    img_filtered = convolution(img_gray, kernel)
    spectrum_filtered = np.fft.fftshift(np.fft.fft2(img_filtered))

    # plot
    plot_imgs(
        [img_rgb, amp_spec(spectrum), img_filtered, amp_spec(spectrum_filtered)],
        ["Robot", "FFT", "Filtered", "Filtered FFT"],
        2,
        cmaps=['gray', 'turbo', 'gray', 'turbo'],
        cbars=[False, True, False, True]
    )

def task_b(img):
    pass

def median(img, kernel_size = 3):
    """ Implements 2D median filter """
    X_img, Y_img = img.shape
    X_ker, Y_ker = kernel_size, kernel_size
    
    img = cv2.copyMakeBorder(img, X_ker-1, X_ker-1, Y_ker-1, Y_ker-1, cv2.BORDER_CONSTANT, value=128)
    
    new_img = np.zeros((X_img, Y_img))
    for x in range(X_ker-1, X_img + X_ker-1):
        for y in range(Y_ker-1, Y_img + Y_ker-1):
            new_img[x-X_ker+1, y-Y_ker+1] = np.median(img[x-X_ker+1:x+1, y-Y_ker+1:y+1])

    return new_img

def task_c(img, kernel_size = 3):
    img_bgr = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # get spectrum
    spectrum = np.fft.fftshift(np.fft.fft2(img_gray))

    # apply filters
    img_filtered = median(img_gray, kernel_size)
    spectrum_filtered = np.fft.fftshift(np.fft.fft2(img_filtered))

    # plot
    plot_imgs(
        [img_rgb, amp_spec(spectrum), img_filtered, amp_spec(spectrum_filtered)],
        ["Robot", "FFT", "Filtered", "Filtered FFT"],
        2,
        cmaps=['gray', 'turbo', 'gray', 'turbo'],
        cbars=[False, True, False, True]
    )

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    # task a
    task_a(robot)
    task_b(robot)
    task_c(robot)
    #task_a(PSS)
    
