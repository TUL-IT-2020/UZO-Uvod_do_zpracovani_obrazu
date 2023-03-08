# By Pytel

import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load image
folder = 'data/'

def find_pictures(folder, file_type: str = ["jpg"]):
    cwd = os.getcwd()
    folder = os.path.join(cwd, folder)
    picture_files = []
    print("Current working directory: {0}, files: ".format(cwd))
    for file in os.listdir(folder):
        # TODO: get file format
        print(file)
        picture_files.append(os.path.join(folder, file))
    return picture_files


def load_images(picture_files: list[str]) -> list[np.ndarray]:
    """ Load images from files
    get:
        picture_files - list of files
    return:
        images - list of images
    """
    images = []
    for file in picture_files:
        bgr = cv2.imread(file)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        images.append(rgb)
    return images


def convert_to_gray(images: list[np.ndarray]) -> list[np.ndarray]:
    gray_images = []
    for image in images:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray_images.append(gray)
    return gray_images


def calculate_histogram(images) -> list:
    histograms = []
    for image in images:
        h, be = np.histogram(image, bins=256, range=(0, 255))
        histograms.append(h)
    return histograms


def histogram_distances_from(histograms, i: int) -> np.ndarray:
    """ Calculate distances from histogram i to all other histograms
    get:
        histograms - list of histograms
        i - index of histogram
    return:
        distances - np.ndarray of distances
    """
    hist = histograms[i]
    distances = []
    for j, h in enumerate(histograms):
        if i == j:
            distances.append(0)
        else:
            distances.append(np.linalg.norm(hist-h))
    distances = np.array(distances)
    return distances


if __name__ == '__main__':
    picture_files = find_pictures(folder)
    picture_files.sort()
    number_of_images = len(picture_files)

    images = load_images(picture_files)

    histograms = calculate_histogram(convert_to_gray(images))

    # show images
    plt.figure()
    print("Sorted images:")
    for i, image in enumerate(images):
        distances = histogram_distances_from(histograms, i)

        # sort distances
        sorted_indices = np.argsort(distances)
        print(sorted_indices)

        # show images
        for j, img_index in enumerate(sorted_indices):
            plt.subplot(number_of_images, number_of_images,
                        number_of_images*i+j+1)
            plt.imshow(images[img_index])

    plt.show()

# END
