
# coding: utf-8


import numpy as np
import pandas as pd

sFile='C:/VKHCG/01-Vermeulen/00-RawData/BuyChoices.txt'
caInputeDF = pd.read_csv(sFile, sep = ";")


# Input = a ranking of 3 different features (TV Size, TV Type, TV Color) with 3(42",47",60")<br>
# , 2 (LCD, Plasma), 3(Red, Blue, Pink) different stimuli types.

print(caInputeDF)

# ## First step is to introduce dummy variables for every stimulus<p>
# There are in total 9 different stimuli, and 18 different combinations

ConjointDummyDF = pd.DataFrame(np.zeros((18,9)), columns=["Rank","A1", "A2", "A3","B1","B2","C1", "C2","C3"])

ConjointDummyDF.Rank = caInputeDF.Rank

for index, row in caInputeDF.iterrows():  
    stimuli1 = str(caInputeDF["Stimulus"].iloc[index][:2])
    stimuli2 = str(caInputeDF["Stimulus"].iloc[index][2:4])
    stimuli3 = str(caInputeDF["Stimulus"].iloc[index][4:6]) 
    
    #print(stimuli1,stimuli2,stimuli3)
    
    stimuliLine=[stimuli1,stimuli2,stimuli3]
    Columns=ConjointDummyDF.columns
    for stimuli in stimuliLine:
        for i in range(len(Columns)):
            if stimuli == Columns[i]:
                ConjointDummyDF.iloc[index, i] = 1

#print(ConjointDummyDF.head())

# ## Insert the proper Stimulus names

fullNames = {"Rank":"Rank", "A1": "42\" (106cm)","A2": "47\" (120cm)","A3": "60\" (152cm)","B1": "Plasma","B2":"LCD","C1":"Blue","C2":"Red","C3": "Pink",}

ConjointDummyDF.rename(columns=fullNames, inplace=True)


#ConjointDummyDF.head()


# ## Estimate Main Effects with a linear regression
# <p>
# 
# There are different ways for parameter estimation beside linear regression depending on what kind of rating you have.<br>
# For example using Probit or Logit is the output is not a rank but a decision (1=chose stimulus, 0 = no choice).

import statsmodels.api as sm


#print(ConjointDummyDF.columns)


X = ConjointDummyDF[[u'42" (106cm)', u'47" (120cm)', u'60" (152cm)', u'Plasma',       u'LCD', u'Red', u'Blue', u'Pink']]
X = sm.add_constant(X)
Y = ConjointDummyDF.Rank
linearRegression = sm.OLS(Y, X). fit()
print(linearRegression.summary())


# ## Part worth values & relative importance of the stimuli
# <p>
# Importance of Stimuli= Max(beta) - Min(beta)
# <br>
# Relative Importance of Stimuli = Importance of Stim / Sum(Importance of all Stimuli)


importance = []
relative_importance = []

rangePerFeature = []

begin = "A"
tempRange = []
for stimuli in fullNames.keys():
    if stimuli[0] == begin:
        tempRange.append(linearRegression.params[fullNames[stimuli]])
    elif stimuli == "Rank":
        rangePerFeature.append(tempRange)
    else:
        rangePerFeature.append(tempRange)
        begin = stimuli[0]
        tempRange = [linearRegression.params[fullNames[stimuli]]]
  

for item in rangePerFeature:
    importance.append( max(item) - min(item))

for item in importance:
    relative_importance.append(100* round(item/sum(importance),3))

partworths = []

item_levels = [1,3,5,8]

for i in range(1,4):
    part_worth_range = linearRegression.params[item_levels[i-1]:item_levels[i]]
    print (part_worth_range)

meanRank = []
for i in ConjointDummyDF.columns[1:]:
    newmeanRank = ConjointDummyDF["Rank"].loc[ConjointDummyDF[i] == 1].mean()
    meanRank.append(newmeanRank)
    
#total Mean or, "basic utility" is used as the "zero alternative"
totalMeanRank = sum(meanRank) / len(meanRank)

partWorths = {}
for i in range(len(meanRank)):
    name = fullNames[sorted(fullNames.keys())[i]]
    partWorths[name] = meanRank[i] - totalMeanRank

print(partWorths)

# ### Summary & Results

print ("Relative Importance of Feature:\n\nMonitor Size:",relative_importance[0], "%","\nType of Monitor:", relative_importance[1], "%", "\nColor of TV:", relative_importance[2], "%\n\n")

print ("--"*30)

print ("Importance of Feature:\n\nMonitor Size:",importance[0],"\nType of Monitor:", importance[1],  "\nColor of TV:", importance[2])

# What would be the optimal product bundle? <p>
# 60", LCD, Red

#As array that looks like X
#Must include Constant!

optBundle = [1,0,0,1,0,1,0,1,0]
print ("The best possible Combination of Stimuli would have the highest rank:",linearRegression.predict(optBundle)[0])


# Or using the Partworths:

#Optimal Bundle:
#42", LCD, Red

optimalWorth = partWorths["60\" (152cm)"] + partWorths["LCD"] + partWorths["Red"]

print ("Choosing the optimal Combination brings the Customer an extra ", optimalWorth, "'units' of utility")
