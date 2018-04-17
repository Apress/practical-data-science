from timezonefinder import TimezoneFinder
tf = TimezoneFinder()

for longitude in range(-180,180,10):
    for latitude in range(-90,90,10):
        timezone_name=tf.closest_timezone_at(lng=longitude, lat=latitude, delta_degree=3)
        if timezone_name != None:
            print(longitude,latitude,timezone_name)