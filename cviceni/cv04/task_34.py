# By Pytel, mothspaws
import cv2
import numpy as np
import matplotlib.pyplot as plt

from my_lib import clear

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
def amp_spec(fft):
    return np.log(np.abs(fft))

def plot_imgs(imgs, titles, rows : int = 1, cmap=None):
    # set plt sizes
    plt.rcParams["figure.figsize"] = (10,2)
    n = len(imgs)
    cols = int(np.ceil(n/rows))
    if cmap != None:
        plt.set_cmap(cmap)
    for i in range(n):
        img = imgs[i]
        plt.subplot(rows, cols, i+1)
        plt.imshow(img) 
        plt.colorbar(fraction=0.046, pad=0.04)
        plt.title(titles[i])
    plt.show()
    plt.waitforbuttonpress()

if __name__ == '__main__':
    plt.ion()
    clear()
    plt.close('all')

    robot_bgr = cv2.imread(robot)
    robot_rgb = cv2.cvtColor(robot_bgr, cv2.COLOR_BGR2RGB)
    gray_robot = cv2.cvtColor(robot_rgb, cv2.COLOR_RGB2GRAY)
    robot_fft = np.fft.fft2(gray_robot)

    plot_imgs(
        [robot_rgb, amp_spec(robot_fft), amp_spec(fftshift(robot_fft))],
        ["Robot", "FFT", "FFTshift"]
    )

    filtHP_bgr = cv2.imread(filtHP)


# END