# -*- coding: utf-8 -*-
import pandas as pd
datafile='C:/VKHCG/01-Vermeulen/00-RawData/PlantGrowth.csv'
data = pd.read_csv(datafile)
 
#Create a boxplot
data.boxplot('weight', by='group', figsize=(12, 8))
 
ctrl = data['weight'][data.group == 'ctrl']
 
grps = pd.unique(data.group.values)
d_data = {grp:data['weight'][data.group == grp] for grp in grps}
 
k = len(pd.unique(data.group))  # number of conditions
N = len(data.values)  # conditions times participants
n = data.groupby('group').size()[0] #Participants in each condition


from scipy import stats
 
F, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])

DFbetween = k - 1
DFwithin = N - k
DFtotal = N - 1

SSbetween = (sum(data.groupby('group').sum()['weight']**2)/n) \
    - (data['weight'].sum()**2)/N

sum_y_squared = sum([value**2 for value in data['weight'].values])
SSwithin = sum_y_squared - sum(data.groupby('group').sum()['weight']**2)/n

SStotal = sum_y_squared - (data['weight'].sum()**2)/N

MSbetween = SSbetween/DFbetween

MSwithin = SSwithin/DFwithin

F = MSbetween/MSwithin

eta_sqrd = SSbetween/SStotal

omega_sqrd = (SSbetween - (DFbetween * MSwithin))/(SStotal + MSwithin)

print(F,p,eta_sqrd,omega_sqrd)