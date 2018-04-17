################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
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
t=0
img=mpimg.imread(sPicName)
for i in plt.colormaps(): 
    sTitle='R8 - Color Map:' + i
    fig=plt.figure(figsize=(10, 10)) 
    plt.title(sTitle)
    imgplot = plt.imshow(img)
    imgplot.set_cmap(i)   
    plt.show()