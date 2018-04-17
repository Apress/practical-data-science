import pandas as pd
import numpy as np
df =pd.DataFrame({'col1':np.random.randn(100),'col2':np.random.randn(100)})
df.hist(layout=(1,2))