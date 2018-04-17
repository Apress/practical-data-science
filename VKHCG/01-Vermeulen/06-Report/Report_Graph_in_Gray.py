################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import numpy as np
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
sImages=[
#        'andrews_curves',
#        'parallel_coordinates',
#        'area',
#        'bar',
#        'hbar',
#        'hexbin',
#        'kde',
#        'line',
#        'pie',
#        'pie_explode',
#        'radviz',
#        'scatter',
#        'scatter_matrix',
#        'TrafficHourly',
#        'TrafficWeekly',
#        'AudiR8Edge1',
#        'AudiR8Edge2',
#        'autocorrelation_plot',
#        'bootstrap_plot',
#        'lag_plot',
#        'contour0',
#        'contour1',
#        'contour2',
#        'contour3',
#        'contour4',
#        'contour5',
        '3DPlot'
        ]
for sImage in sImages:
    fnameIn=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/'+sImage+'.png'
    fnameOut=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/'+sImage+'_gray.png'
    ################################################################
    image = Image.open(fnameIn).convert("L")
    arr = np.asarray(image) 
    ################################################################
    nDPI=600
    nDPISave=600
    h=arr.shape[0]
    w=arr.shape[1]   
    fig =plt.figure(figsize=(w/nDPI, h/nDPI), dpi=nDPI,frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ################################################################
    plt.imshow(arr, cmap='gray', aspect='auto')
    fig.savefig(fnameOut, dpi=nDPISave, transparent=True, \
                bbox_inches='tight', pad_inches=0)
    ################################################################