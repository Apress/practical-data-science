################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
################################################################
Base='C:/VKHCG'
sInputFileName='Good-or-Bad.csv'
sOutputFileNameA='Good-or-Bad-05-A.csv'
sOutputFileNameB='Good-or-Bad-05-B.csv'
sOutputFileNameC='Good-or-Bad-05-C.csv'
sOutputFileNameD='Good-or-Bad-05-D.csv'
sOutputFileNameE='Good-or-Bad-05-E.csv'
Company='01-Vermeulen'
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + 'VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
### Import Warehouse
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + sInputFileName
print('Loading :',sFileName)
RawData=pd.read_csv(sFileName,header=0)

print('################################')  
print('## Raw Data Values')  
print('################################')  
print(RawData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sInputFileName
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.fillna(RawData.mean())
################################################################
print('################################')  
print('## Test Data Values- Mean')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileNameA
TestData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.fillna(RawData.median())
################################################################
print('################################')  
print('## Test Data Values - Median')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileNameB
TestData.to_csv(sFileName, index = False)
################################################################
################################################################
TestData=RawData.fillna(RawData.mode())
################################################################
print('################################')  
print('## Test Data Values - Mode')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileNameC
TestData.to_csv(sFileName, index = False)
################################################################
################################################################
TestData=RawData.fillna(RawData.min())
################################################################
print('################################')  
print('## Test Data Values - Minumum')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileNameD
TestData.to_csv(sFileName, index = False)
################################################################
################################################################
TestData=RawData.fillna(RawData.max())
################################################################
print('################################')  
print('## Test Data Values - Maximum')  
print('################################')  
print(TestData)
print('################################')   
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sFileDir + '/' + sOutputFileNameE
TestData.to_csv(sFileName, index = False)
################################################################
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
################################################################