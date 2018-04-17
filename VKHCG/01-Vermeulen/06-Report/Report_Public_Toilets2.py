################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import folium
import pandas as pd
from bng_to_latlon import OSGB36toWGS84
import webbrowser
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileNameIn=Base+'/01-Vermeulen/00-RawData/public-toilets.csv'
sFileNameOut=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/colchester_toilets_clusters.html'
# Load map centred on Colchester
uk = folium.Map(location=[51.8860942,0.8336077], zoom_start=10, control_scale=True)
 
# Load locally stored colchester public toilets data
os.chdir('C:/VKHCG/01-Vermeulen/00-RawData')
toilets = pd.read_csv("public-toilets.csv")
 
t=0
for each in toilets.iterrows(): 
    datalist=list(OSGB36toWGS84(each[1]['Geo X'],each[1]['Geo Y']))
    t+=1
    if t==1:
        data=[datalist]
    else:
        data.append(datalist)

# create a marker cluster called "Public toilet cluster"
marker_cluster = folium.plugins.FastMarkerCluster(data).add_to(uk)

#add a marker for each toilet, add it to the cluster, not the map
for each in toilets.iterrows():  
    print(list([each[1]['Geo X'],each[1]['Geo Y']]))
    print(list(OSGB36toWGS84(each[1]['Geo X'],each[1]['Geo Y'])))
    folium.Marker(list(OSGB36toWGS84(each[1]['Geo X'],each[1]['Geo Y'])), popup=each[1]['Street Address']).add_to(marker_cluster)
 
# we can also add a marker directly to the map, outside of the clustering
folium.Marker([51.8860942,0.8336077], popup="not included in marker cluster",icon=folium.Icon(color='red',icon='info-sign')).add_to(uk)
 
# Save map
print('Create HTML page')
uk.save(sFileNameOut)
webbrowser.open('file://' + os.path.realpath(sFileNameOut))