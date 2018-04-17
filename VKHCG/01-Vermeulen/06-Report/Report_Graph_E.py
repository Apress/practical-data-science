# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib as ml
import numpy as np
from matplotlib import pyplot as plt
ml.style.use('ggplot')


price = pd.Series(np.random.randn(250).cumsum(),\
                  index=pd.date_range('2017-1-1', periods=250, freq='B'))
ma = price.rolling(20).mean()
mstd = price.rolling(20).std()

plt.figure(figsize=(12, 5))
plt.plot(price.index, price, 'k')
plt.plot(ma.index, ma, 'b')
plt.fill_between(mstd.index, ma-2*mstd, ma+2*mstd, color='b', alpha=0.2)