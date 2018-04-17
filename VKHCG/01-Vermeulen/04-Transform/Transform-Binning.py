import numpy
binNum=10
data = numpy.random.random(10000)
bins = numpy.linspace(0, 1, binNum+1)
#######################################################################
digitized = numpy.digitize(data, bins)
bin_means = [data[digitized == i].mean() for i in range(1, len(bins))]
print('\nDigitize')
for b in range(len(bin_means)):
    print('Bin:',b+1,'->',bin_means[b])
#######################################################################
bin_means2 = (numpy.histogram(data, bins, weights=data)[0] /
             numpy.histogram(data, bins)[0])
print('\nHistogram')
for b in range(len(bin_means)):
    print('Bin:',b+1,'->',bin_means2[b])
#######################################################################