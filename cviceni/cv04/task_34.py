# By Pytel
import os
import cv2
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

# TODO: imlepment fftshift
def fftshift(fft):
    return np.fft.fftshift(fft)

if __name__ == '__main__':
    plt.ion()
    if os.name == 'nt':
        clear = lambda: os.system('cls')
    elif os.name == 'posix':
        clear = lambda: os.system('clear')
    clear()
    plt.close('all')

    robot_bgr = cv2.imread(robot)
    robot_rgb = cv2.cvtColor(robot_bgr, cv2.COLOR_BGR2RGB)
    gray_robot = cv2.cvtColor(robot_rgb, cv2.COLOR_RGB2GRAY)
    robot_fft = np.fft.fft2(gray_robot)

    plot_imgs(
        [robot_rgb, np.log(np.abs(fftshift(robot_fft)))],
        ["Robot", "FFT"]
    )

    filtHP_bgr = cv2.imread(filtHP)


# END