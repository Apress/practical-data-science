import os
import sys
import matplotlib.pyplot as plt
from numpy.random import randn
import pandas as pd
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
sInputFileName='/02-Assess/01-EDS/02-Python/Assess-DE-Billboard-Visitor.csv'
sOutputFileName='Assess-DE-Billboard-Visitor.png'
Company='02-Krennwallner'
################################################################
sDataBaseDir=Base + '/' + Company + '/06-Report/01-EDS/02-Python'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
### Import Billboard Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
BillboardData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('Loaded Billboard :',BillboardData.columns.values)

plotdataraw=BillboardData[['BillboardLatitude','BillboardLongitude']]

plotdatafix=plotdataraw.drop_duplicates(subset=None, keep='first', inplace=False)

print('Loaded Plot :',plotdatafix.columns.values,plotdatafix.shape)

plotdata=plotdatafix

x = plotdata['BillboardLatitude']
y = plotdata['BillboardLongitude']

fig=plt.figure(num=None, figsize=(100, 100), dpi=100, facecolor='w', edgecolor='k')
fig.suptitle('Practical Data Science', fontsize=300)
plt.title("Germany - Billboard Locations", fontsize=150)
plt.xlabel('Latitude', fontsize=200)
plt.ylabel('Longitude', fontsize=200)
plt.scatter(x, y,s=80, marker=(4, 1),color='red')
plt.subplots_adjust(left=0.15)
#plt.show()
################################################################
print('################################')
print('Storing :', sFileName)
print('################################')
sFileName=sDataBaseDir + '/' + sOutputFileName
fig.savefig(sFileName, dpi=100)
################################################################