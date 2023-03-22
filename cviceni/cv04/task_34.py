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

    # get spectrum
    spectrum = fftshift(np.fft.fft2(gray_robot))

    picture = robot
    filter_files = [filtHP, filtHP1]
    graph_titles = []
    graph_pictures = []
    for filter_file in filter_files:
        # read filter
        filter = cv2.imread(filter_file)
        # apply filters
        filtered_fft = np.multiply(spectrum, filter)
        # fft to image
        filtered_img = np.fft.ifft2(filtered_fft)
        graph_titles.append(filter_file)
        graph_titles.append(picture)
        graph_pictures.append(filtered_fft)
        graph_pictures.append(filtered_img)

    plot_imgs(
        graph_pictures,
        graph_titles,
        2
    )

    #filters = [filtDP, filtDP1]


# END