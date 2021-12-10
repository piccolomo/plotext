from plotext._utility.data import replace

def to_gray_rgb(matrix): # from a standard matrix to a matrix of gray rgb colors
    if matrix == []:
        return []
    M, m = max([max(el) for el in matrix]), min([min(el) for el in matrix])
    gray_rgb = lambda el: tuple([int(255 * ((el - m) / (M - m)))] * 3)
    matrix = [[gray_rgb(el) for el in l] for l in matrix]
    return matrix

def resize_image(image, size, keep_ratio, resample): # it resize an image to the desired size, mantaining or not its size ratio and adding or not a pixel averaging factor with resample = True
    osize = image.size
    oratio = image.size[1] / image.size[0]
    
    nsize = [osize[0], osize[1] / 2] if keep_ratio else osize
    nratio = 2 * nsize[1] / nsize[0]

    nsize = replace(size, nsize)
    nratio = 2 * nsize[1] / nsize[0]

    if nratio > oratio and keep_ratio:
        nsize = [nsize[0], nsize[0] * oratio / 2] if nratio > oratio and keep_ratio else nsize
    elif nratio < oratio and keep_ratio:        nsize = [2 * nsize[1] / oratio, nsize[1]]
    nratio = 2 * nsize[1] / nsize[0]

    image = image if nsize == osize else image.resize(map(int, nsize), resample=resample)
    return image

def image_to_matrix(image): # from image to a matrix of pixels
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels


# old version based on numpy
# def image_to_matrix(image): # from image to a matrix of pixels
#     matrix = np.array(image)
#     if type(matrix[0][0]) == np.ndarray or type(el) == list:
#         matrix = [[tuple(el) for el in l] for l in matrix]
#     return matrix


# def matrix_to_image(matrix): # from a matrix of pixels to an image, never used so far
#     from PIL.Image import fromarray
#     import numpy as np
#     return fromarray(np.uint8(matrix))

