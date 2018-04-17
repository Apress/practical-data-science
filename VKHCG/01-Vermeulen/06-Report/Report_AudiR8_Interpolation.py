################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sPicName=Base+'/01-Vermeulen/00-RawData/AudiR8.png'
nSize=15
################################################################
img = Image.open(sPicName)
img.thumbnail((64, 64), Image.ANTIALIAS)
InterpolationSet=[ 'none', 'nearest', 'bilinear', \
                  'bicubic', 'spline16', \
                  'spline36', 'hanning', \
                  'hamming', 'hermite', \
                  'kaiser', 'quadric', \
                  'catrom', 'gaussian', \
                  'bessel', 'mitchell', \
                  'sinc', 'lanczos']
t=0
for InterpolationSelect in InterpolationSet:
    t+=1
    plt.figure(figsize=(nSize, nSize))
    sTitle= '(' + str(t) + ') Interpolation:' + InterpolationSelect
    plt.title(sTitle)
    imgplot = plt.imshow(img, interpolation=InterpolationSelect)
    plt.show()
################################################################
print('### Done!! ############################################')
################################################################