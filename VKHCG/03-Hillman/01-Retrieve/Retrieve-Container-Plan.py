################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
################################################################
ContainerFileName='Retrieve_Container.csv'
BoxFileName='Retrieve_Box.csv'
ProductFileName='Retrieve_Product.csv'
Company='03-Hillman'
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileDir=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
### Create the Containers
################################################################
containerLength=range(1,21)
containerWidth=range(1,10)
containerHeigth=range(1,6)
containerStep=1
c=0
for l in containerLength:
    for w in containerWidth:
        for h in containerHeigth:
            containerVolume=(l/containerStep)*(w/containerStep)*(h/containerStep)
            c=c+1
            ContainerLine=[('ShipType', ['Container']), 
                       ('UnitNumber', ('C'+format(c,"06d"))),
                       ('Length',(format(round(l,3),".4f"))),
                       ('Width',(format(round(w,3),".4f"))), 
                       ('Height',(format(round(h,3),".4f"))),
                       ('ContainerVolume',(format(round(containerVolume,6),".6f")))]
            if c==1:
               ContainerFrame = pd.DataFrame.from_items(ContainerLine) 
            else:
                ContainerRow = pd.DataFrame.from_items(ContainerLine)
                ContainerFrame = ContainerFrame.append(ContainerRow)
            ContainerFrame.index.name = 'IDNumber'
                   
print('################')   
print('## Container') 
print('################')
print('Rows :',ContainerFrame.shape[0])
print('Columns :',ContainerFrame.shape[1])
print('################')
################################################################
sFileContainerName=sFileDir + '/' + ContainerFileName 
ContainerFrame.to_csv(sFileContainerName, index = False) 
################################################################
## Create valid Boxes with packing foam
################################################################
boxLength=range(1,21)
boxWidth=range(1,21)
boxHeigth=range(1,21)
packThick=range(0,6)
boxStep=10
b=0
for l in boxLength:
    for w in boxWidth:
        for h in boxHeigth:
            for t in packThick:
                boxVolume=round((l/boxStep)*(w/boxStep)*(h/boxStep),6)
                productVolume=round(((l-t)/boxStep)*((w-t)/boxStep)*((h-t)/boxStep),6)
                if productVolume > 0:
                    b=b+1
                    BoxLine=[('ShipType', ['Box']), 
                       ('UnitNumber', ('B'+format(b,"06d"))),
                       ('Length',(format(round(l/10,6),".6f"))),
                       ('Width',(format(round(w/10,6),".6f"))), 
                       ('Height',(format(round(h/10,6),".6f"))),
                       ('Thickness',(format(round(t/5,6),".6f"))),
                       ('BoxVolume',(format(round(boxVolume,9),".9f"))),
                       ('ProductVolume',(format(round(productVolume,9),".9f")))]
                    if b==1:
                       BoxFrame = pd.DataFrame.from_items(BoxLine) 
                    else:
                        BoxRow = pd.DataFrame.from_items(BoxLine)
                        BoxFrame = BoxFrame.append(BoxRow)
                    BoxFrame.index.name = 'IDNumber'
                    
print('#################')   
print('## Box')   
print('#################')
print('Rows :',BoxFrame.shape[0])
print('Columns :',BoxFrame.shape[1])
print('#################')
################################################################
sFileBoxName=sFileDir + '/' + BoxFileName 
BoxFrame.to_csv(sFileBoxName, index = False) 
################################################################
## Create valid Product
################################################################
productLength=range(1,21)
productWidth=range(1,21)
productHeigth=range(1,21)
productStep=10
p=0
for l in productLength:
    for w in productWidth:
        for h in productHeigth:
            productVolume=round((l/productStep)*(w/productStep)*(h/productStep),6)
            if productVolume > 0:
                p=p+1
                ProductLine=[('ShipType', ['Product']), 
                   ('UnitNumber', ('P'+format(p,"06d"))),
                   ('Length',(format(round(l/10,6),".6f"))),
                   ('Width',(format(round(w/10,6),".6f"))), 
                   ('Height',(format(round(h/10,6),".6f"))),
                   ('ProductVolume',(format(round(productVolume,9),".9f")))]
                if p==1:
                   ProductFrame = pd.DataFrame.from_items(ProductLine) 
                else:
                    ProductRow = pd.DataFrame.from_items(ProductLine)
                    ProductFrame = ProductFrame.append(ProductRow)
                BoxFrame.index.name = 'IDNumber'
                    
print('#################')   
print('## Product')   
print('#################')
print('Rows :',ProductFrame.shape[0])
print('Columns :',ProductFrame.shape[1])
print('#################')
################################################################
sFileProductName=sFileDir + '/' + ProductFileName 
ProductFrame.to_csv(sFileProductName, index = False) 
################################################################
#################################################################
print('### Done!! ############################################')
#################################################################