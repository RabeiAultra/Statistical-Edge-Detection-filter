from __future__ import division
from gaussian_filter import gaussian
from numpy import array, zeros, abs, sqrt, arctan2, arctan, pi, real
from numpy.fft import fft2, ifft2
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def gradient(im):
    # Sobel operator
    op1 = array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]])
    op2 = array([[-1, -2, -1],
                 [ 0,  0,  0],
                 [ 1,  2,  1]])
    #op1=op1*2;
    #op2=op2*2;
    kernel1 = zeros(im.shape)
    kernel1[:op1.shape[0], :op1.shape[1]] = op1
    kernel1 = fft2(kernel1)

    kernel2 = zeros(im.shape)
    kernel2[:op2.shape[0], :op2.shape[1]] = op2
    kernel2 = fft2(kernel2)

    fim = fft2(im)
    Gx = real(ifft2(kernel1 * fim)).astype(float)
    Gy = real(ifft2(kernel2 * fim)).astype(float)

    G = sqrt(Gx**2 + Gy**2)
    Theta = arctan(Gy, Gx) * 180 / pi
    return G, Theta

