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

def rotation_mask(image, kernel_size=3):
    output_image = np.zeros(image.shape)
    h0,h1 = (kernel_size-1)//2, (kernel_size-1)//2 
    new_image = np.pad(image,((h0,h0),(h1,h1)),'constant',constant_values=(0,0))
    variancies = np.zeros(new_image.shape)
    means = np.zeros(new_image.shape)
    for y, row in enumerate(new_image):
        if(y == 0 or y == new_image.shape[0]):
            continue
        for x, pixel in enumerate(row):
            if (x == 0 or x == new_image.shape[1]):
                continue
            window = new_image[y-1:y+2, x-1:x+2]
            variancies[y, x] = np.var(window)
            means[y, x] = np.mean(window)
    
            
    for y, row in enumerate(image):
        if(y == 0 or y == image.shape[0]):
            continue
        for x, pixel in enumerate(row):
            if (x == 0 or x == image.shape[1]):
                continue
            window = variancies[y-1:y+2, x-1:x+2]
            window_mean = means[y-1:y+2, x-1:x+2]
            window[1,1] = float('inf')
            tmp = np.unravel_index(window.argmin(), window.shape)
            tmp_min = window_mean[tmp]
            output_image[y,x] = tmp_min
    return output_image

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
    
