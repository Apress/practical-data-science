################################################################
# -*- coding: utf-8 -*-
################################################################
import os
import pandas as pd
from math import radians, cos, sin, asin, sqrt
################################################################
def haversine(lon1, lat1, lon2, lat2,stype):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    if stype == 'km':
        r = 6371 # Radius of earth in kilometers
    else:
        r = 3956 # Radius of earth in miles
    d=round(c * r,3)
    return d
################################################################
InputFileName='GB_Postcode_Warehouse.csv'
OutputFileName='Retrieve_Incoterm_Chain_GB_Warehouse.csv'
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
### Import Warehouse
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + InputFileName
print('###########')
print('Loading :',sFileName)
Warehouse=pd.read_csv(sFileName,header=0,low_memory=False)

WarehouseGood=Warehouse[Warehouse.latitude != 0]

WarehouseGood['Warehouse_Name']=WarehouseGood.apply(lambda row:
            'WH-' + row['postcode']
            ,axis=1)
WarehouseGood.drop('id', axis=1, inplace=True)
WarehouseGood.drop('postcode', axis=1, inplace=True)
################################################################    
WarehouseFrom=WarehouseGood.head(100)
for i in range(WarehouseFrom.shape[1]):
    oldColumn=WarehouseFrom.columns[i]
    newColumn=oldColumn + '_from'
    WarehouseFrom.rename(columns={oldColumn: newColumn}, inplace=True)    
WarehouseFrom.insert(3,'Keys', 1)
################################################################    
WarehouseTo=WarehouseGood.head(100)
for i in range(WarehouseTo.shape[1]):
    oldColumn=WarehouseTo.columns[i]
    newColumn=oldColumn + '_to'
    WarehouseTo.rename(columns={oldColumn: newColumn}, inplace=True)    
WarehouseTo.insert(3,'Keys', 1)
################################################################    
WarehouseCross=pd.merge(right=WarehouseFrom,
                       left=WarehouseTo,
                        how='outer',
                        on='Keys')

WarehouseCross.drop('Keys', axis=1, inplace=True)
   
WarehouseCross.insert(0,'Incoterm', 'DDP')

WarehouseCross['DistanceBetweenKilometers'] = WarehouseCross.apply(lambda row: 
    haversine(
            row['longitude_from'],
            row['latitude_from'],
            row['longitude_to'],
            row['latitude_to'],
            'km')
            ,axis=1)

WarehouseCross['DistanceBetweenMiles'] = WarehouseCross.apply(lambda row: 
    haversine(
            row['longitude_from'],
            row['latitude_from'],
            row['longitude_to'],
            row['latitude_to'],
            'miles')
            ,axis=1)

WarehouseCross.drop('longitude_from', axis=1, inplace=True) 
WarehouseCross.drop('latitude_from', axis=1, inplace=True) 
WarehouseCross.drop('longitude_to', axis=1, inplace=True) 
WarehouseCross.drop('latitude_to', axis=1, inplace=True)
 
WarehouseCrossClean=WarehouseCross[WarehouseCross.DistanceBetweenKilometers !=0]

print('###########')
print('Rows :',WarehouseCrossClean.shape[0])
print('Columns :',WarehouseCrossClean.shape[1])
print('###########')
################################################################

sFileName=sFileDir + '/' + OutputFileName
WarehouseCrossClean.to_csv(sFileName, index = False)

#################################################################
print('### Done!! ############################################')
#################################################################