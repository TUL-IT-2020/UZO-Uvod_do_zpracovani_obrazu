# By Pytel
"""
1) Naprogramujte Laplaceův, Sobelův a Kirschův hranový detektor pro 
obrázek cv06c_robotC.bmp. 
 
2) Zobrazte původní obrázek, výsledek z hranového detektoru a spektrum 
pro každý z hranových detektorů. 
"""

import sys
import cv2
import matplotlib.pyplot as plt
sys.path.append('../')
sys.path.append('../my_libs/')
sys.path.append('../my_libs/img/')
from my_libs.fft import *
from my_libs.tools import *
from my_libs.colors import *
from my_libs.img.filters import *
from my_libs.img.processing import *

def run_and_plot_task(img, algorithm, task_name="Task"):
    # test if file exists
    if not os.path.isfile(img):
        raise FileNotFoundError(Red + "File:", Blue + str(img), Red + "not found!" + NC)

    print(Green + "Running:", Blue + task_name, Green + "..." + NC)

    img_bgr = cv2.imread(img)

    # convert img
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # get spectrum
    spectrum = np.fft.fftshift(np.fft.fft2(img_gray))

    # apply algorithm
    img_filtered = algorithm(img_gray)
    # get spectrum
    spectrum_filtered = np.fft.fftshift(np.fft.fft2(img_filtered))

    # plot
    plot_imgs(
        [img_gray, amp_spec(spectrum), img_filtered, amp_spec(spectrum_filtered)],
        ["Original", "FFT", "Edge Detecion", "Detection FFT"],
        2,
        cmaps=['gray', 'turbo', 'turbo', 'turbo'],
        cbars=[False, True, True, True],
        window_name=task_name
    )
    plt.close()


robot = "cv06_robotC.bmp"

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    run_and_plot_task(robot, laplace, "Laplace")    
    run_and_plot_task(robot, sobel, "Sobel")
    run_and_plot_task(robot, kirsch, "Kirsch")
    
    print(Green + "Done." + NC)

# END
