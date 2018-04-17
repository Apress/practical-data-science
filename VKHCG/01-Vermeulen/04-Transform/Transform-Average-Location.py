import numpy as np
import pandas as pd

LatitudeData = pd.Series(np.array(range(-90,91,1)))
LongitudeData = pd.Series(np.array(range(-180,181,1)))

LatitudeSet=LatitudeData.sample(10)
LongitudeSet=LongitudeData.sample(10)

LatitudeAverage = np.average(LatitudeSet)
LongitudeAverage = np.average(LongitudeSet)

print('Latitude')
print(LatitudeSet)
print('Latitude (Avg):',LatitudeAverage)
print('##############')
print('Longitude')
print(LongitudeSet)
print('Longitude (Avg):', LongitudeAverage)