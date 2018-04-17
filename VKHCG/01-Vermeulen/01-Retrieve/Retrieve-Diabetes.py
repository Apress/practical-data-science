################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
from sklearn import datasets
import pandas as pd
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/IP_DATA_CORE.csv'
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,
  usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
################################################################
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
diabetes = datasets.load_diabetes()
diabetesData=pd.DataFrame(diabetes.data)
for i in range(diabetesData.shape[1]):
    oldName=i
    newName='Result'+str(i)
    diabetesData.rename(columns={oldName: newName}, inplace=True)
print(diabetesData)
diabetesTarget=pd.DataFrame(diabetes.target)
for i in range(diabetesTarget.shape[1]):
    oldName=i
    newName='Target'+str(i)
    diabetesTarget.rename(columns={oldName: newName}, inplace=True)
print(diabetesTarget)
################################################################
diabetesFull=diabetesData
diabetesFull['Target']=diabetesTarget['Target0']
print(diabetesFull)
################################################################
sFileName1=sFileDir + '/Retrieve_Diabetes_Data.csv'
sFileName2=sFileDir + '/Retrieve_Diabetes_Target.csv'
sFileName3=sFileDir + '/Retrieve_Diabetes_Full.csv'
diabetesData.to_csv(sFileName1, index = False, encoding="latin-1")
diabetesTarget.to_csv(sFileName2, index = False, encoding="latin-1")
diabetesFull.to_csv(sFileName3, index = False, encoding="latin-1")
################################################################
print('### Done!! ############################################')
################################################################