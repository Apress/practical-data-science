# -*- coding: utf-8 -*-
import os
import pandas as pd
from folium import folium
from pandas import compat
from folium.plugins import MarkerCluster

os.chdir('../VKHCG/01-Vermeulen/00-RawData') 
compat.PY3 = True
 
universities = pd.read_csv("uk_universities_locations2.csv")
 
uk = folium.Map(location=[universities.lat.mean(axis=0),universities.lon.mean(axis=0)], zoom_start=5)
marker_cluster = MarkerCluster("Universities").add_to(uk)
#add a marker for each university
for each in universities.iterrows():  
    folium.Marker(list([each[1]['lat'],each[1]['lon']]),popup=each[1]['Name']).add_to(marker_cluster)
 
uk.save("./universities.html")