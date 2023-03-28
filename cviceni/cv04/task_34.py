# By Pytel, mothspaws
import cv2
import numpy as np
import matplotlib.pyplot as plt

from my_lib import *

"""
3) Z obrázku cv04c_robotC.bmp spočítejte 2D DFT (fft2 = np.fft.fft2(gray)) 
a zobrazte amplitudové spektrum, upravte kvadranty spektra, aby se nízké 
frekvence nacházely ve středu (vytvořte si pro tyto účely funkci).

4) Filtrujte obraz pomocí filtrů DP, HP, jako masky použijte obrázky 
cv04c_filtHP.bmp, cv04c_filtHP1.bmp, cv04c_filtDP.bmp, cv04c_filtDP1.bmp. 
Obrázky si upravte jako matice s hodnotami 0, 1. 
Výsledky zobrazte spolu se spektrem. 
"""

robot = "cv04c_robotC.bmp"
filtHP = "cv04c_filtHP.bmp"
filtHP1 = "cv04c_filtHP1.bmp"
filtDP = "cv04c_filtDP.bmp"
filtDP1 = "cv04c_filtDP1.bmp"

def task03():
    robot_bgr = cv2.imread(robot)
    robot_rgb = cv2.cvtColor(robot_bgr, cv2.COLOR_BGR2RGB)
    gray_robot = cv2.cvtColor(robot_rgb, cv2.COLOR_RGB2GRAY)
    robot_fft = np.fft.fft2(gray_robot)

    plot_imgs(
        [robot_rgb, amp_spec(robot_fft), amp_spec(fftshift(robot_fft))],
        ["Robot", "FFT", "FFTshift"],
        cbars=[False, True, True]
    )

def filter_img(img, filter_files):
    img_bgr = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    # get spectrum
    spectrum = fftshift(np.fft.fft2(img_gray))
    
    graph_titles = []
    graph_pictures = []
    color_maps = []
    for filter_file in filter_files:
        # read filter
        filter = cv2.imread(filter_file)
        filter = cv2.cvtColor(filter, cv2.COLOR_BGR2GRAY)
        # apply filters
        filtered_fft = np.multiply(spectrum, filter)
        # fft to image
        filtered_img = np.fft.ifft2(filtered_fft)

        graph_titles.append(filter_file)
        graph_titles.append(img)
        graph_pictures.append(amp_spec(filtered_fft))
        graph_pictures.append(np.abs(filtered_img))
        color_maps.append('turbo')
        color_maps.append('gray')

    plot_imgs(
        graph_pictures,
        graph_titles,
        2,
        color_maps
    )


if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    # task 03
    task03()

    # task 04
    filter_img(robot, [filtDP, filtDP1])
    plt.close('all')
    filter_img(robot, [filtHP, filtHP1])


# END