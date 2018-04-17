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
sFileNameOut=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/colchester_toilets.html'
# Load map centred on Colchester
uk = folium.Map(location=[51.8860942,0.8336077], zoom_start=10)

# Load locally stored colchester public toilets data
toilets = pd.read_csv(sFileNameIn)

#add a marker for each toilet
for each in toilets.iterrows():  
    print(list([each[1]['Geo X'],each[1]['Geo Y']]))
    print(list(OSGB36toWGS84(each[1]['Geo X'],each[1]['Geo Y'])))
    folium.Marker(list(OSGB36toWGS84(each[1]['Geo X'],each[1]['Geo Y'])), \
                  popup=each[1]['Street Address']).add_to(uk)
    
# Save map
print('Create HTML page')
uk.save(sFileNameOut)
webbrowser.open('file://' + os.path.realpath(sFileNameOut))