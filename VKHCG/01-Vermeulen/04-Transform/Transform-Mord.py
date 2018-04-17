# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/StudentData.csv'
################################################################

StudentFrame = pd.read_csv(sFileName,header=0)

StudentFrame.columns = ["sname", "gre", "gpa", "prestige","admit","QR","VR","gpatrue"]
StudentSelect=StudentFrame[["admit", "gre", "gpa", "prestige"]]
print('Record select:',StudentSelect.shape[0])

df=StudentSelect

#df=StudentSelect.drop_duplicates(subset=None, keep='first', inplace=False)
#print('Records Unique:', df.shape[0])

print(df.columns)

print(df.describe())

print(df.std())

print(pd.crosstab(df['admit'], df['prestige'], rownames=['admit']))

# plot all of the columns

df.hist()
pl.tight_layout()
pl.show()

# dummify rank
dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')
print(dummy_ranks.head())

# create a empty data frame for the regression
cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.loc[:, 'prestige_1':])
print(data.head())

# Add the intercept
data['intercept'] = 1.00

#Train Model
train_cols = data.columns[1:]

logit = sm.Logit(data['admit'], data[train_cols])

# fit the model
result = logit.fit(maxiter=500)

# Results
print('Results')
print(result.summary())


# Investigate at the confidence interval of each coeffecient
print(result.conf_int())

# odds ratios only
print(np.exp(result.params))
  
# odds ratios and 95% CI
params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
print(np.exp(conf))

# instead of generating all possible values of GRE and GPA, you're only
# to use an evenly spaced range of 10 values from the min to the max
# this a a simple way of binning data to reduce complexity.
gres = np.linspace(data['gre'].min(), data['gre'].max(), 10)
print(gres)
gpas = np.linspace(data['gpa'].min(), data['gpa'].max(), 10)
print(gpas)


#define the cartesian function
def cartesian(arrays, out=None):
    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype
    
    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = int(n / arrays[0].size)
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out

# enumerate all possibilities
combos = pd.DataFrame(cartesian([gres, gpas, [1, 2, 3, 4], [1,]]))
# recreate the dummy variables
combos.columns = ['gre', 'gpa', 'prestige', 'intercept']
dummy_ranks = pd.get_dummies(combos['prestige'], prefix='prestige')
dummy_ranks.columns = ['prestige_1', 'prestige_2', 'prestige_3', 'prestige_4']


# keep only what we need for making predictions
cols_to_keep = ['gre', 'gpa', 'prestige', 'intercept']
combos = combos[cols_to_keep].join(dummy_ranks.loc[:, 'prestige_1':])

# make predictions on the enumerated dataset
combos['admit_pred'] = result.predict(combos[train_cols])

print(combos.head())


def isolate_and_plot(variable):
    # isolate gre and class rank
    grouped = pd.pivot_table(combos, values=['admit_pred'], index=[variable, 'prestige'],
                aggfunc=np.mean)
    # make a plot
    colors = 'rbgyrbgy'
    for col in combos.prestige.unique():
        plt_data = grouped.loc[grouped.index.get_level_values(1)==col]
        pl.plot(plt_data.index.get_level_values(0), plt_data['admit_pred'], color=colors[int(col)])

    pl.xlabel(variable)
    pl.ylabel("P(admit=1)")
    pl.legend(['1', '2', '3', '4'], loc='upper left', title='Prestige')
    pl.title("Prob(admit=1) isolating " + variable + " and presitge")
    pl.show()

isolate_and_plot('gre')
isolate_and_plot('gpa')

