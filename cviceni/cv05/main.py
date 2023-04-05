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
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')
from my_libs.tools import *
from my_libs.colors import *
from my_libs.fft import *
from my_libs.img.processing import *
import my_libs.img.filters as filters

robot = "cv05_robotS.bmp"
PSS = "cv05_PSS.bmp"

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
    plt.close()

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    # task a
    print(Green + "Running filter:", Blue + "mean", Green + "..." + NC)
    run_and_plot_task(robot, filters.mean)
    # run_and_plot_task(PSS, filters.mean)

    # task b
    print(Green + "Running filter:", Blue + "rotation mask", Green + "..." + NC)
    run_and_plot_task(robot, filters.rotation_mask)
    # run_and_plot_task(PSS, filters.rotation_mask)

    # task c
    print(Green + "Running filter:", Blue + "median", Green + "..." + NC)
    run_and_plot_task(robot, filters.median)
    # run_and_plot_task(PSS, filters.median)

    print(Green + "Done." + NC)

#END
