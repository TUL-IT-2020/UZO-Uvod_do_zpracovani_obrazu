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

robot = "cv05_robotS.bmp"
PSS = "cv05_PSS.bmp"

def task_a(img):
    img_bgr = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # get spectrum
    spectrum = np.fft.fftshift(np.fft.fft2(img_gray))

    # apply filters
    # TODO: apply filters
    img_filtered = img_gray
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

def task_c(img):
    pass

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    # task a
    task_a(robot)
    #task_a(PSS)
    
