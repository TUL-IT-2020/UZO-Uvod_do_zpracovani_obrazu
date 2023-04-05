# By Pytel

import cv2
import numpy as np
import matplotlib.pyplot as plt
import functional as func

# TODO:
class IMG(np.ndarray):
    # TODO:
    def __init__(self, img : np.ndarray):
        super().__init__(img)

    def convolution(self, kernel):
        """ Implements 2D convolution 

        Args:
            kernel : kernel to convolute

        Returns:
            new_img : convoluted image
        """
        return func.convolution(self._img, kernel)


def plot_imgs(
        imgs, titles, rows : int = 1, cmaps=None, 
        cbars=None, figsize=(8,6), window_name="Graph"
    ):
    """ Plot images
    
    Args:
        imgs : list of images
        titles : list of titles
        rows : number of rows
        cmap : color map
        figsize : size of figure
        window_name : name of window
    """
    plt.figure(window_name, figsize=figsize)
    #plt.rcParams["figure.figsize"] = figsize
    n = len(imgs)
    cols = int(np.ceil(n/rows))
    for i in range(n):
        img = imgs[i]
        plt.subplot(rows, cols, i+1)
        plt.imshow(img) 
        plt.title(titles[i])
        if cmaps != None and cmaps[i] != None:
            plt.set_cmap(cmaps[i])
        if cbars != None and cbars[i]:
            plt.colorbar(fraction=0.046, pad=0.04)
    plt.show()
    plt.waitforbuttonpress()

# TODO:
if __name__ == "__main__":
    img_path = "test_img.bmp"
    cv2_img = cv2.imread(img_path)
    # type
    print(type(cv2_img))
    img = IMG(cv2_img)
    print(type(img))
    # plot
    plt.imshow(img)
