# By Pytel, mothspaws
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

def mean_filter(img, kernel_size = 3):
    kernel = np.ones((kernel_size, kernel_size)) / kernel_size**2
    return convolution(img, kernel)

def rotation_mask(img, kernel_size = 3):
    """ Implements 2D rotation mask filter """
    X_img, Y_img = img.shape
    img_padded = cv2.copyMakeBorder(img, kernel_size-1, kernel_size-1, kernel_size-1, kernel_size-1, cv2.BORDER_CONSTANT, value=128)
    new_img = np.zeros((X_img, Y_img))

    def get_mask_orientations():
        masks = [
            np.array([[1, 1, 1], [0, 1, 0], [0, 0, 0]]),
            np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]]),
            np.array([[0, 0, 1], [0, 1, 1], [0, 0, 1]]),
            np.array([[0, 0, 0], [0, 1, 1], [0, 1, 1]]),
            np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
            np.array([[0, 0, 0], [1, 1, 0], [1, 1, 0]]),
            np.array([[1, 0, 0], [1, 1, 0], [1, 0, 0]]),
            np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
        ]
        return masks

    masks = get_mask_orientations()

    for x in range(X_img):
        for y in range(Y_img):
            variances = []
            for mask in masks:
                region = img_padded[x:x+kernel_size, y:y+kernel_size]
                masked_region = region * mask
                variances.append(np.var(masked_region))
            
            best_mask_idx = np.argmin(variances)
            best_mask = masks[best_mask_idx]
            new_img[x, y] = np.mean(img_padded[x:x+kernel_size, y:y+kernel_size] * best_mask)
    return new_img

def median(img, kernel_size = 3):
    """ Implements 2D median filter """
    X_img, Y_img = img.shape
    X_ker, Y_ker = kernel_size, kernel_size
    
    img = cv2.copyMakeBorder(img, X_ker-1, X_ker-1, Y_ker-1, Y_ker-1, cv2.BORDER_CONSTANT, value=128)
    
    new_img = np.zeros((X_img, Y_img))
    for x in range(X_ker-1, X_img + X_ker-1):
        for y in range(Y_ker-1, Y_img + Y_ker-1):
            """
            # take cros from image
            y_axis = img[x, y-Y_ker+1:y+1]
            x_axis = img[x-X_ker+1:x+1, y]
            # get median
            new_img[x-X_ker+1, y-Y_ker+1] = np.median(np.concatenate((y_axis, x_axis)))
            """
            new_img[x-X_ker+1, y-Y_ker+1] = np.median(img[x-X_ker+1:x+1, y-Y_ker+1:y+1])

    return new_img

def run_and_plot_task(img, algorithm, kernel_size = 3):
    img_bgr = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # get spectrum
    spectrum = np.fft.fftshift(np.fft.fft2(img_gray))

    # apply filters
    img_filtered = algorithm(img_gray, kernel_size)
    spectrum_filtered = np.fft.fftshift(np.fft.fft2(img_filtered))

    # plot
    plot_imgs(
        [img_rgb, amp_spec(spectrum), img_filtered, amp_spec(spectrum_filtered)],
        ["Original", "FFT", "Filtered", "Filtered FFT"],
        2,
        cmaps=['gray', 'turbo', 'gray', 'turbo'],
        cbars=[False, True, False, True]
    )

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    # task a
    # run_and_plot_task(robot, mean_filter)
    # run_and_plot_task(PSS, mean_filter)
    # task b
    run_and_plot_task(robot, rotation_mask)
    # run_and_plot_task(PSS, rotation_mask)
    # task c
    # run_and_plot_task(robot, median)
    # run_and_plot_task(PSS, median)
    
