################################################################
# -*- coding: utf-8 -*-
################################################################
import os
import pandas as pd
from geopy.distance import vincenty
################################################################
InputFileName='GB_Postcode_Warehouse.csv'
OutputFileName='Retrieve_GB_Warehouse.csv'
Company='03-Hillman'
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileDir=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + InputFileName
print('###########')
print('Loading :',sFileName)
Warehouse=pd.read_csv(sFileName,header=0,low_memory=False)

WarehouseClean=Warehouse[Warehouse.latitude != 0]
WarehouseGood=WarehouseClean[WarehouseClean.longitude != 0]

WarehouseGood.drop_duplicates(subset='postcode', keep='first', inplace=True)

WarehouseGood.sort_values(by='postcode', ascending=1)
################################################################
sFileName=sFileDir + '/' + OutputFileName
WarehouseGood.to_csv(sFileName, index = False)
################################################################

WarehouseLoop = WarehouseGood.head(20)

for i in range(0,WarehouseLoop.shape[0]):
    print('Run :',i,' =======>>>>>>>>>>',WarehouseLoop['postcode'][i])
    WarehouseHold = WarehouseGood.head(10000)
    WarehouseHold['Transaction']=WarehouseHold.apply(lambda row:
                'WH-to-WH' 
                ,axis=1)
    OutputLoopName='Retrieve_Route_' + 'WH-' + WarehouseLoop['postcode'][i] + '_Route.csv'
    
    WarehouseHold['Seller']=WarehouseHold.apply(lambda row:
                'WH-' + WarehouseLoop['postcode'][i]
                ,axis=1)
    
    WarehouseHold['Seller_Latitude']=WarehouseHold.apply(lambda row:
                WarehouseHold['latitude'][i]
                ,axis=1)
    WarehouseHold['Seller_Longitude']=WarehouseHold.apply(lambda row:
                WarehouseLoop['longitude'][i]
                ,axis=1)
    
    WarehouseHold['Buyer']=WarehouseHold.apply(lambda row:
                'WH-' + row['postcode']
                ,axis=1)
    
    WarehouseHold['Buyer_Latitude']=WarehouseHold.apply(lambda row:
                row['latitude']
                ,axis=1)
    WarehouseHold['Buyer_Longitude']=WarehouseHold.apply(lambda row:
                row['longitude']
                ,axis=1)
        
    WarehouseHold['Distance']=WarehouseHold.apply(lambda row: round(
        vincenty((WarehouseLoop['latitude'][i],WarehouseLoop['longitude'][i]),
                 (row['latitude'],row['longitude'])).miles,6)
       ,axis=1)
    
    WarehouseHold.drop('id', axis=1, inplace=True)
    WarehouseHold.drop('postcode', axis=1, inplace=True)
    WarehouseHold.drop('latitude', axis=1, inplace=True)
    WarehouseHold.drop('longitude', axis=1, inplace=True)
    ################################################################
    sFileLoopName=sFileDir + '/' + OutputLoopName
    WarehouseHold.to_csv(sFileLoopName, index = False)
#################################################################
print('### Done!! ############################################')
#################################################################