# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:34:45 2021

@author: abc
"""

"""


 blind/referenceless image spatial quality evaluator (BRISQUE)


"""

import numpy as np
import cv2
from skimage import io, img_as_float
import imquality.brisque as brisque

#Read our image
img = img_as_float(io.imread("BSE.jpg", as_gray=True))

#Apply BRISQUE
score = brisque.score(img)
print("Brisque score = ", score)

#############################################################

#Let's check the BRISQUE score of noisy image
import numpy as np
from skimage import io, img_as_float
import imquality.brisque as brisque

#Read our noisy image
img = img_as_float(io.imread("BSE_50sigma_noisy.jpg", as_gray=True))

#Apply BRISQUE
score = brisque.score(img)
print("Brisque score = ",score)


#################################################################

#Now let us check BRISQUE scores for a bunch of blurred images

img0 = img_as_float(io.imread("BSE.jpg", as_gray=True))
img25 = img_as_float(io.imread("BSE_1sigma_blur.jpg", as_gray=True))
img50 = img_as_float(io.imread("BSE_2sigma_blur.jpg",as_gray=True))
img75 = img_as_float(io.imread("BSE_5sigma_blur.jpg", as_gray=True))
img100 = img_as_float(io.imread("BSE_5sigma_blur.jpg", as_gray=True))
img200 = img_as_float(io.imread("BSE_10sigma_blur.jpg", as_gray=True))

score0 = brisque.score(img0)
score25 = brisque.score(img25)
score50 = brisque.score(img50)
score75 = brisque.score(img75)
score100 = brisque.score(img100)
score200 = brisque.score(img200)

print("BRISQUE Score of 0 blur = ", score0)
print("BRISQUE Score of 1 sigma blur = ", score25)
print("BRISQUE Score of 2 sigma blur = ", score50)
print("BRISQUE Score of 3 sigma blur = ", score75)
print("BRISQUE Score of 5 sigma blur = ", score100)
print("BRISQUE Score of 10 sigma blur = ", score200)

#Peak signal to noise ratio (PSNR) is Not a good metric.

from skimage.metrics import peak_signal_noise_ratio

psnr_25 = peak_signal_noise_ratio(img0, img25)
psnr_50 = peak_signal_noise_ratio(img0, img50)
psnr_75 = peak_signal_noise_ratio(img0, img75)
psnr_100 = peak_signal_noise_ratio(img0, img100)
psnr_200 = peak_signal_noise_ratio(img0, img200)

print("PSNR for 1 sigma blur = ", psnr_25)
print("PSNR for 2 sigma blur = ", psnr_50)
print("PSNR for 3 sigma blur = ", psnr_75)
print("PSNR for 5 sigma blur = ", psnr_100)
print("PSNR for 10 sigma blur = ", psnr_200)







