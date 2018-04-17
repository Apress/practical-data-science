################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os

from math import radians, cos, sin, asin, sqrt

from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import DBSCAN

import matplotlib.pyplot as plt
import pandas as pd
################################################################
def haversine(lonlat1, lonlat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lat1, lon1 = lonlat1
    lat2, lon2 = lonlat2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
################################################################
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print('Loading :',sFileName)
scolumns=("Latitude","Longitude")

RawData = pd.read_csv(sFileName,usecols=scolumns,header=0,low_memory=False)

#print(RawData)
X=RawData.sample(n=1000)

distance_matrix = squareform(pdist(X, (lambda u,v: haversine(u,v))))
print(distance_matrix)

db = DBSCAN(eps=0.2, min_samples=2, metric='precomputed', algorithm='auto')
y_db = db.fit_predict(distance_matrix)

X['cluster'] = y_db
C = X.cluster.unique()

fig=plt.figure(1, figsize=(20, 20))
plt.title('Estimated number of clusters: %d' % len(C))
plt.scatter(X['Latitude'], X['Longitude'], c=X['cluster'],marker='D')
plt.show()
fig.savefig('C:/VKHCG/01-Vermeulen/04-Transform/01-EDS/02-Python/Location_Cluster.jpg')
plt.close(fig)

################################################################
print('### Done!! ############################################')
################################################################