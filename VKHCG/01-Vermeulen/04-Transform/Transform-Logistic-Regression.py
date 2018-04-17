################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
Company='01-Vermeulen'
################################################################
sFileDir=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
sFileName=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python/Retrieve_Iris_Full.csv'
print('Loading :',sFileName)
DataRaw=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
################################################################
sSteps=['02-Assess','03-Process','04-Transform']
for sStep in sSteps:    
    ################################################################
    sFileDir=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ################################################################
    sFile=sStep[3:]+'_Isis.csv'
    sFileName=Base + '/01-Vermeulen/'+sStep+'/01-EDS/02-Python/'+sFile
    print('Storing :',sFileName)
    DataRaw.to_csv(sFileName, index = False, encoding="latin-1")
################################################################
# import data to ecosystem
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

h = .02  # step size in the mesh

logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(8, 6))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.title('Shipping Box Sizes')
plt.xlabel('Box Length')
plt.ylabel('Box Width')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()