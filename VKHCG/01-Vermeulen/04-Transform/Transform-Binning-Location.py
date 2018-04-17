import numpy as np
LatitudeData = np.array(range(-90,90,1))
LongitudeData = np.array(range(-180,180,1))

LatitudeBins = np.array(range(-90,90,45))
LongitudeBins = np.array(range(-180,180,60))

LatitudeDigitized = np.digitize(LatitudeData, LatitudeBins)
LongitudeDigitized = np.digitize(LongitudeData, LongitudeBins)

LatitudeBinMeans = [LatitudeData[LatitudeDigitized == i].mean() for i in range(1, len(LatitudeBins))]
LongitudeBinMeans = [LongitudeData[LongitudeDigitized == i].mean() for i in range(1, len(LongitudeBins))]
print(LatitudeBinMeans)
print(LongitudeBinMeans)
#######################################################################
LatitudeBinMeans2 = (np.histogram(LatitudeData, LatitudeBins, weights=LatitudeData)[0] /
             np.histogram(LatitudeData, LatitudeBins)[0])
LongitudeBinMeans2 = (np.histogram(LongitudeData, LongitudeBins, weights=LongitudeData)[0] /
             np.histogram(LongitudeData, LongitudeBins)[0])
print(LatitudeBinMeans2)
print(LongitudeBinMeans2)