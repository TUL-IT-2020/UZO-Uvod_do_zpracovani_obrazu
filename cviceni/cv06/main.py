# By Pytel
"""
1) Naprogramujte Laplaceův, Sobelův a Kirschův hranový detektor pro 
obrázek cv06c_robotC.bmp. 
 
2) Zobrazte původní obrázek, výsledek z hranového detektoru a spektrum 
pro každý z hranových detektorů. 
"""

import sys
import cv2
sys.path.append('../')
from cv04.my_lib import *
from cv03.graphic import *
from my_colors import *


def laplace(img):
    kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]])
    kernel = np.array([
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1]])

    return convolution(img, kernel)

def sobel(img):
    kernels = []
    kernels.append(np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]]))
    kernels.append(np.array([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]))
    kernels.append(np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]))
    kernels.append(np.array([
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2]]))
    kernels.append(np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]]))
    kernels.append(np.array([
        [0, -1, -2],
        [1, 0, -1],
        [2, 1, 0]]))
    kernels.append(np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]]))
    edges = []
    for kernel in kernels:
        edges.append(convolution(img, kernel))
    edges_np = np.array(edges)
    return np.max(edges_np, axis=0)

def kirsch(img):
    kernels = []
    kernels.append(np.array([
        [-5, -5, -5],
        [3, 0, 3],
        [3, 3, 3]]))
    kernels.append(np.array([
        [-5, -5, 3],
        [-5, 0, 3],
        [3, 3, 3]]))
    kernels.append(np.array([
        [-5, 3, 3],
        [-5, 0, 3],
        [-5, 3, 3]]))
    kernels.append(np.array([
        [3, 3, 3],
        [-5, 0, 3],
        [-5, -5, 3]]))
    kernels.append(np.array([
        [3, 3, 3],
        [3, 0, 3],
        [-5, -5, -5]]))
    kernels.append(np.array([
        [3, 3, 3],
        [3, 0, -5],
        [3, -5, -5]]))
    kernels.append(np.array([
        [3, 3, -5],
        [3, 0, -5],
        [3, 3, -5]]))
    kernels.append(np.array([
        [3, -5, -5],
        [3, 0, -5],
        [3, 3, 3]]))
    edges = []
    for kernel in kernels:
        edges.append(convolution(img, kernel))
    edges_np = np.array(edges)
    return np.max(edges_np, axis=0)

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