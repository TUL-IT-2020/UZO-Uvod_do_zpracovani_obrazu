# By Pytel

import numpy as np

def generate_rotation_matrix(center : tuple() = (0,0), angle: float = 0) -> np.array:
    """ Generate rotation matrix
    """
    #cv2.getRotationMatrix2D(center, angle, scale)
    angle = np.deg2rad(angle)
    cos = np.cos(angle)
    sin = np.sin(angle)
    x, y = center
    M = np.array([
        [cos, -sin, x*(1-cos)+y*sin],
        [sin, cos, y*(1-cos)-x*sin]]
    )
    return M

def generate_translation_matrix(move): 
    """ Generate movement matrix
    """
    x_move, y_move = move
    M = np.array([
        [1, 0, x_move],
        [0, 1, y_move],
        [0, 0, 1]
        ]
    )
    return M

def transform_coords(point : tuple(), M : np.array) -> tuple():
    """ Project point
    """
    x, y = point
    vector = np.array([x, y, 1])
    vector = np.dot(M, vector)
    return (vector[0], vector[1])

def valid_point(coord : tuple(), shape : tuple()) -> bool:
    """ Validate point coordinates
    """
    x, y = coord
    X, Y, _ = shape
    if x < 0 or x >= X or y < 0 or y >= Y:
        return False
    return True

def project_pixels(source, M, destination) -> np.array:
    """ Project pixels
    get:
        source - source image
        M - inverse transformation matrix
        destination - blank destination image
    return:
        destination - transformed image
    """
    X, Y, _ = destination.shape
    for x in range(X):
        for y in range(Y):
            coord = transform_coords((x, y), M)
            y_orig = int(coord[1])
            x_orig = int(coord[0])
            if valid_point(coord, source.shape):
                destination[x, y] = source[x_orig, y_orig]
    return destination

def warpAffine(image, M, dsize):
    """ Warp affine
    """
    #cv2.warpAffine(image, M, dsize)
    rows, cols = dsize
    dst = np.zeros((rows, cols, 3), np.uint8)
    dst = project_pixels(image, M, dst)
    return dst