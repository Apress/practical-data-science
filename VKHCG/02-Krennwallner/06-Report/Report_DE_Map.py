import geopandas as gpd
from matplotlib import pyplot as pp
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
southern_world = world.cx[:, :0]
#southern_world.plot(figsize=(10, 3));
#world.plot(figsize=(10, 6));
deworld=world[world['name']=='Germany']
deworld.plot(figsize=(10, 6));
pp.show()