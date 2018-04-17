################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
from sklearn import datasets
import pandas as pd
import numpy as np
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
iris = datasets.load_iris()
print(type(iris))
irisData=pd.DataFrame(iris.data)
for i in range(irisData.shape[1]):
    oldName=i
    newName='Result'+str(i)
    irisData.rename(columns={oldName: newName}, inplace=True)
print(irisData)
irisTarget=pd.DataFrame(iris.target)
for i in range(irisTarget.shape[1]):
    oldName=i
    newName='Target'+str(i)
    irisTarget.rename(columns={oldName: newName}, inplace=True)
print(irisTarget)
################################################################
irisFull=pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
print(irisFull)
################################################################
sFileName0=sFileDir + '/Retrieve_Iris_Data.json'
irisFull.to_json(sFileName0)
################################################################
sFileName1=sFileDir + '/Retrieve_Iris_Data.csv'
sFileName2=sFileDir + '/Retrieve_Iris_Target.csv'
sFileName3=sFileDir + '/Retrieve_Iris_Full.csv'
irisData.to_csv(sFileName1, index = False, encoding="latin-1")
irisTarget.to_csv(sFileName2, index = False, encoding="latin-1")
irisFull.to_csv(sFileName3, index = False, encoding="latin-1")
################################################################
print('### Done!! ############################################')
################################################################