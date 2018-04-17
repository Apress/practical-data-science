################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import numpy
import scipy
from scipy import ndimage
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sPicNameIn=Base+'/01-Vermeulen/00-RawData/AudiR8.png'
sPicNameOut=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/AudiR8Edge2.png'
################################################################
im = scipy.misc.imread(sPicNameIn)
im = im.astype('int32')
dx = ndimage.sobel(im, 0) # horizontal derivative
dy = ndimage.sobel(im, 1) # vertical derivative
mag = numpy.hypot(dx, dy) # magnitude
mag *= 255.0 / numpy.max(mag) # normalize (Q&D)
scipy.misc.imsave(sPicNameOut, mag)

import matplotlib.pyplot as plt
from PIL import Image

imageIn = Image.open(sPicNameIn)
plt.figure(figsize=(10, 10))
imgplot = plt.imshow(imageIn)

imageTest = Image.open(sPicNameOut)
plt.figure(figsize=(10, 10))
imgplot = plt.imshow(imageTest)