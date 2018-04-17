################################################################
import sys
import os
import sqlite3 as sq
import pandas as pd
import datetime
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
Company='04-Clark'
################################################################
sDataBaseDir=Base + '/' + Company + '/01-Retrieve/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataBaseDir + '/clark.db'
conn = sq.connect(sDatabaseName)
################################################################
start = pd.datetime(1900, 1, 1)
end = pd.datetime(2018, 1, 1)
date1Data= pd.DataFrame(pd.date_range(start, end))
################################################################
start = pd.datetime(2000, 1, 1)
end = pd.datetime(2020, 1, 1)
date2Data= pd.DataFrame(pd.date_range(start, end))
################################################################
dateData=date1Data.append(date2Data)
dateData.rename(columns={0 : 'FinDate'},inplace=True)
################################################################
print('################')  
sTable='Retrieve_Date'
print('Storing :',sDatabaseName,' Table:',sTable)
dateData.to_sql(sTable, conn, if_exists="replace")
print('################')  
################################################################
print('################################')
print('Rows : ',dateData.shape[0], ' records')
print('################################')
################################################################
t=0
for h in range(24):
    for m in range(60):
        for s in range(5):
            nTime=[str(datetime.timedelta(hours=h,minutes=m,seconds=30))]
            if h == 0 and m == 0:
                timeData= pd.DataFrame(nTime)
            else:
                time1Data=  pd.DataFrame(nTime)
                timeData= timeData.append(time1Data)
timeData.rename(columns={0 : 'FinTime'},inplace=True)
################################################################
print('################')  
sTable='Retrieve_Time'
print('Storing :',sDatabaseName,' Table:',sTable)
timeData.to_sql(sTable, conn, if_exists="replace")
print('################')  
################################################################
print('################################')
print('Rows : ',timeData.shape[0], ' records')
print('################################')
################################################################
print('### Done!! ############################################')
################################################################