################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sCompanies=['01-Vermeulen','02-Krennwallner','03-Hillman','04-Clark']
Steps=['00-RawData','01-Retrieve','02-Assess','03-Process'\
       ,'04-Transform','05-Organise','06-Report']
SubSteps=['01-EDS/01-R','01-EDS/02-Python']
for i in range(len(sCompanies)):
    for j in range(len(Steps)):
        for k in range(len(SubSteps)):
            sDataBaseDir=Base + '/' + sCompanies[i] + '/' + \
            Steps[j] + '/' + SubSteps[k]
            print('#####################################')
            print('Check:',sDataBaseDir)
            if not os.path.exists(sDataBaseDir):
                print('Make:',sDataBaseDir)
                os.makedirs(sDataBaseDir)
                print('#####################################')
################################################################
for i in range(len(sCompanies)):
    for j in range(len(Steps)):
        print('#####################################')
        sDataBaseDir=Base + '/' + sCompanies[i] + '/' + \
        Steps[j] + '/SQLite' 
        if not os.path.exists(sDataBaseDir):
            print('Make:',sDataBaseDir)
            os.makedirs(sDataBaseDir)
        print('#####################################')   
        DatabaseName=sDataBaseDir + '/'  + sCompanies[i][3:] + '.db' 
        print('Check:',DatabaseName)
        if os.path.exists(DatabaseName):
            print('Remove:',DatabaseName)
            os.remove(DatabaseName)
        print('#####################################')
################################################################
print('#####################################')
sDataBaseDir=Base + '/88-DV' 
if not os.path.exists(sDataBaseDir):
    print('Make:',sDataBaseDir)
    os.makedirs(sDataBaseDir)
print('#####################################')   
DatabaseName=sDataBaseDir + '/datavault.db' 
print('Check:',DatabaseName)
if os.path.exists(DatabaseName):
    print('Remove:',DatabaseName)
    os.remove(DatabaseName)
print('#####################################')
################################################################
print('#####################################')
sDataBaseDir=Base + '/99-DW' 
if not os.path.exists(sDataBaseDir):
    print('Make:',sDataBaseDir)
    os.makedirs(sDataBaseDir)
print('#####################################')   
DatabaseName=sDataBaseDir + '/datawarehouse.db' 
print('Check:',DatabaseName)
if os.path.exists(DatabaseName):
    print('Remove:',DatabaseName)
    os.remove(DatabaseName)
print('#####################################')
################################################################