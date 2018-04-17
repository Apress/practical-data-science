# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
for i in plt.colormaps(): 
    sTitle='Color Map:' + i
    fig=plt.figure(figsize=(10, 10)) 
    plt.title(sTitle)
    imgplot = plt.imshow(np.random.rand(10,10))
    imgplot.set_cmap(i)   
    plt.show()