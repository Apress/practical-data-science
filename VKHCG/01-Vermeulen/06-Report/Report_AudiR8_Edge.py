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
sPicNameIn=Base+'/01-Vermeulen/00-RawData/AudiR8.png'
sPicNameOut=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/AudiR8Edge1.png'

imageIn = Image.open(sPicNameIn)
fig1=plt.figure(figsize=(10, 10))
fig1.suptitle('Audi R8', fontsize=20)
imgplot = plt.imshow(imageIn)

mask=imageIn.convert("L")
th=49 # the value has to be adjusted for an image of interest 
imageOut = mask.point(lambda i: i < th and 255)
imageOut.save(sPicNameOut) 

imageTest = Image.open(sPicNameOut)
fig2=plt.figure(figsize=(10, 10))
fig2.suptitle('Audi R8 Edge', fontsize=20)
imgplot = plt.imshow(imageTest)