################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
sDatabaseName=Base + '/01-Vermeulen/00-RawData/SQLite/Vermeulen.db'
conn = sq.connect(sDatabaseName)
print('Loading :',sDatabaseName)
IP_DATA_ALL=pd.read_sql_query("select * from IP_DATA_ALL;", conn)
################################################################
print('Rows:', IP_DATA_ALL.shape[0])
print('Columns:', IP_DATA_ALL.shape[1])
print('### Raw Data Set #####################################')
for i in range(0,len(IP_DATA_ALL.columns)):
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print('### Fixed Data Set ###################################')
IP_DATA_ALL_FIX=IP_DATA_ALL
for i in range(0,len(IP_DATA_ALL.columns)):
    cNameOld=IP_DATA_ALL_FIX.columns[i] + '     '
    cNameNew=cNameOld.strip().replace(" ", ".")
    IP_DATA_ALL_FIX.columns.values[i] = cNameNew
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
################################################################
#print(IP_DATA_ALL_FIX.head())
################################################################
print('################') 
print('Fixed Data Set with ID')
print('################') 
IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
print('################') 
print(IP_DATA_ALL_with_ID.head())
print('################') 

sTable2='Retrieve_IP_DATA'
IP_DATA_ALL_with_ID.to_sql(sTable2,conn, index_label="RowID", if_exists="replace")

################################################################
print('### Done!! ############################################')
################################################################