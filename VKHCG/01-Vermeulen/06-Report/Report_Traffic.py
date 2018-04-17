# -*- coding: utf-8 -*-

sFileName='C:/VKHCG/01-Vermeulen/00-RawData/traffic-violations.json'

import ijson

with open(sFileName, 'r') as f:
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)
    
print(columns[0])
#
#column_names = [col["fieldName"] for col in columns]
#print(column_names)
#
#good_columns = [
#    "date_of_stop", 
#    "time_of_stop", 
#    "agency", 
#    "subagency",
#    "description",
#    "location", 
#    "latitude", 
#    "longitude", 
#    "vehicle_type", 
#    "year", 
#    "make", 
#    "model", 
#    "color", 
#    "violation_type",
#    "race", 
#    "gender", 
#    "driver_state", 
#    "driver_city", 
#    "dl_state",
#    "arrest_type"
#]

#data = []
#with open(sFileName, 'r') as f:
#    objects = ijson.items(f, 'data.item')
#    for row in objects:
#        selected_row = []
#        for item in good_columns:
#            selected_row.append(row[column_names.index(item)])
#        data.append(selected_row)
#        
#print(data[0])
#
#import pandas as pd
#
#stops = pd.DataFrame(data, columns=good_columns)
#
#stops["color"].value_counts()
#
#print(stops["arrest_type"].value_counts())
#
#import numpy as np
#
#def parse_float(x):
#    try:
#        x = float(x)
#    except Exception:
#        x = 0
#    return x
#stops["longitude"] = stops["longitude"].apply(parse_float)
#stops["latitude"] = stops["latitude"].apply(parse_float)
#
#import datetime
#def parse_full_date(row):
#    date = datetime.datetime.strptime(row["date_of_stop"], "%Y-%m-%dT%H:%M:%S")
#    time = row["time_of_stop"].split(":")
#    date = date.replace(hour=int(time[0]), minute = int(time[1]), second = int(time[2]))
#    return date
#
#stops["date"] = stops.apply(parse_full_date, axis=1)
#
#import matplotlib.pyplot as plt
#
#plt.hist(stops["date"].dt.weekday, bins=6)
#
#plt.hist(stops["date"].dt.hour, bins=24)
#
#last_year = stops[stops["date"] > datetime.datetime(year=2015, month=2, day=18)]
#
#print(last_year.shape)
#
#morning_rush = last_year[(last_year["date"].dt.weekday < 5) & (last_year["date"].dt.hour > 5) & (last_year["date"].dt.hour < 10)]
#print(morning_rush.shape)
#
#import folium
#from folium import plugins
#
#stops_map = folium.Map(location=[39.0836, -77.1483], zoom_start=11)
#marker_cluster = folium.MarkerCluster().add_to(stops_map)
#for name, row in morning_rush.iloc[:1000].iterrows():
#    folium.Marker([row["longitude"], row["latitude"]], popup=row["description"]).add_to(marker_cluster)
#stops_map.create_map('stops.html')
#print(stops_map)
#
#stops_heatmap = folium.Map(location=[39.0836, -77.1483], zoom_start=11)
#stops_heatmap.add_children(plugins.HeatMap([[row["longitude"], row["latitude"]] for name, row in morning_rush.iloc[:1000].iterrows()]))
#stops_heatmap.save("heatmap.html")
#print(stops_heatmap)