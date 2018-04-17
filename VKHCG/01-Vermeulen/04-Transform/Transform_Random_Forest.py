from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import sys
import os
import datetime as dt
import calendar as cal
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + 'VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
basedate = dt.datetime(2018,1,1,0,0,0)
################################################################
Company='04-Clark'
InputFileName='Process_WIKI_UPS.csv'
InputFile=Base+'/'+Company+'/03-Process/01-EDS/02-Python/' + InputFileName
ShareRawData=pd.read_csv(InputFile,header=0,\
                         usecols=['Open','Close','UnitsOwn'], \
                         low_memory=False)
ShareRawData.index.names = ['ID']
ShareRawData['nRow'] = ShareRawData.index
ShareRawData['TradeDate']=ShareRawData.apply(lambda row:\
            (basedate - dt.timedelta(days=row['nRow'])),axis=1)
ShareRawData['WeekDayName']=ShareRawData.apply(lambda row:\
            (cal.day_name[row['TradeDate'].weekday()])\
             ,axis=1)
ShareRawData['WeekDayNum']=ShareRawData.apply(lambda row:\
            (row['TradeDate'].weekday())\
             ,axis=1)
ShareRawData['sTarget']=ShareRawData.apply(lambda row:\
            'true' if row['Open'] < row['Close'] else 'false'\
            ,axis=1)

print(ShareRawData.head())
# Create a dataframe with the two feature variables
sColumns=['Open','Close','WeekDayNum']
df = pd.DataFrame(ShareRawData, columns=sColumns)

# View the top 5 rows
print(df.head())
#==============================================================================

df2 = pd.DataFrame(['sTarget'])
df2.columns =['WeekDayNum']

#==============================================================================
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
# Create two new dataframes, one with the training rows, one with the test rows
train, test = df[df['is_train']==True], df[df['is_train']==False]

# Show the number of observations for the test and training dataframes
print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:',len(test))

# Preprocess Data

# Create a list of the feature column's names
features = df.columns[:3]

# View features
print(features)

y = pd.factorize(train['WeekDayNum'])[0]

# View target
print(y)

#Train The Random Forest Classifier

# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the Classifier to take the training features and learn how they relate
# to the training y (Week Day Number)
clf.fit(train[features], y)

#Apply Classifier To Test Data

# Apply the Classifier we trained to the test data (which, remember, it has never seen before)
clf.predict(test[features])

# View the predicted probabilities of the first 10 observations
print(clf.predict_proba(test[features])[0:10])

#Evaluate Classifier

preds = clf.predict(test[features])[3:4]

# View the PREDICTED Week Day Number for the first ten observations
print('PREDICTED Week Number:',preds[0:10])

# View the ACTUAL WeekDayName for the first ten observations
print(test['WeekDayNum'].head(10))

# Create confusion matrix
c=pd.crosstab(df2['WeekDayNum'], preds, rownames=['Actual Week Day Number'], colnames=['Predicted Week Day Number'])
print(c)
# View a list of the features and their importance scores
print(list(zip(train[features], clf.feature_importances_)))