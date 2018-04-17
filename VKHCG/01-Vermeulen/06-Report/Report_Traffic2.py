# -*- coding: utf-8 -*-

################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import datetime
import pandas as pd
from folium.plugins import FastMarkerCluster, HeatMap
from folium import Marker, Map
import matplotlib.pyplot as plt
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

sFileName=Base+'/01-Vermeulen/00-RawData/Traffic_Violations.csv'

good_columns = [
    'Date Of Stop', 
    'Time Of Stop', 
    'Agency', 
    'SubAgency',
    'Description',
    'Location', 
    'Latitude', 
    'Longitude', 
    'VehicleType', 
    'Year', 
    'Make', 
    'Model', 
    'Color', 
    'Violation Type',
    'Race', 
    'Gender', 
    'Driver State', 
    'Driver City', 
    'DL State',
    'Arrest Type'
    ]

df = pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")

df.fillna(value=0, inplace=True)

print(df.shape)

stopsRaw = pd.DataFrame(df, columns=good_columns)

stops=stopsRaw

print(stops.head())

print(stops["Color"].value_counts())

print(stops['Arrest Type'].value_counts())


def parse_float(x):
    try:
        x = float(x)
    except Exception:
        x = 0.0
    x = round(x,6)
    return x
stops['Longitude'] = stops['Longitude'].apply(parse_float)
stops['Latitude'] = stops['Latitude'].apply(parse_float)


def parse_full_date(row):
    date = datetime.datetime.strptime(row['Date Of Stop'], "%m/%d/%Y")
    time = row['Time Of Stop'].split(":")
    date = date.replace(hour=int(time[0]), minute = int(time[1]), second = int(time[2]))
    return date

stops["date"] = stops.apply(parse_full_date, axis=1)


plt.figure(figsize=(10, 10))
plt.hist(stops["date"].dt.weekday, bins=6)
sFileNamePNG=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/TrafficWeekly.png'
plt.savefig(sFileNamePNG, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 10))
plt.hist(stops["date"].dt.hour, bins=24)
sFileNamePNG=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/TrafficHourly.png'
plt.savefig(sFileNamePNG, bbox_inches='tight')
plt.show()

last_year = stops[stops["date"] > datetime.datetime(year=2015, month=2, day=18)]

print(last_year.shape)

morning_rush = pd.DataFrame(last_year[(last_year["date"].dt.weekday < 5) & (last_year["date"].dt.hour > 5) & (last_year["date"].dt.hour < 10)])
print(morning_rush.shape)

t=0
for i in range(morning_rush.shape[0]):
    try:
        sLongitude=morning_rush["Longitude"][i]
        sLongitude=float(sLongitude)
    except Exception:
        sLongitude=float(0.0)
        
    try:
        sLatitude=morning_rush["Latitude"][i]
        sLatitude=float(sLatitude)
    except Exception:
        sLatitude=float(0.0)
        
    try:
        sDescription=morning_rush["Violation Type"][i]
        sDescription=sDescription[:20]
    except Exception:
        sDescription='*'
    
    if sLongitude != 0.0 and sLatitude != 0.0:
        #print(t,sLongitude,sLatitude)
        DataClusterList=list([sLatitude, sLongitude])
        DataPointList=list([sLatitude, sLongitude, sDescription])
        t+=1
        if t==1:
            DataCluster=[DataClusterList]
            DataPoint=[DataPointList]
        else:
            DataCluster.append(DataClusterList)
            DataPoint.append(DataPointList)
data=DataCluster
pins=pd.DataFrame(DataPoint)
pins.columns = [ 'Latitude','Longitude','Description']

stops_map1 = Map(location=[39.0836, -77.1483], zoom_start=10)
marker_cluster = FastMarkerCluster(data).add_to(stops_map1)
sFileNameHtml=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/morning_rush_stops1.html'
stops_map1.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))

stops_map2 = Map(location=[39.0836, -77.1483], zoom_start=10)
for name, row in pins.iloc[:100].iterrows():
    Marker([row["Latitude"],row["Longitude"]], popup=row["Description"]).add_to(stops_map2)
sFileNameHtml=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/morning_rush_stops2.html'
stops_map2.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))

stops_heatmap = Map(location=[39.0836, -77.1483], zoom_start=10)
stops_heatmap.add_child(HeatMap([[row["Latitude"], row["Longitude"]] for name, row in pins.iloc[:100].iterrows()]))
sFileNameHtml=Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/morning_rush_heatmap.html'
stops_heatmap.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
print('### Done!! ############################################')
################################################################