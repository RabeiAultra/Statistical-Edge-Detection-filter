from __future__ import division
from gaussian_filter import gaussian
from gradient import gradient
from nonmax_suppression import maximum
from numpy import array, zeros, max
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def thresholding(im):
    thres  = zeros(im.shape)
    strong = 9.0
    weak   = 4
    mmax = max(im)
    lo, hi = 0.1 * mmax, 0.8 * mmax
    strongs = []
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            px = im[i][j]
            if px >= hi:
                thres[i][j] = strong
                strongs.append((i, j))
            elif px >= lo:
                thres[i][j] = weak
    return thres, strongs
