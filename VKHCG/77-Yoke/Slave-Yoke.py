################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import sqlite3 as sq
from pandas.io import sql
import pandas as pd
from multiprocessing import Process
################################################################
def prepecosystem():
    if sys.platform == 'linux': 
        Base=os.path.expanduser('~') + '/VKHCG'
    else:
        Base='C:/VKHCG'
    ############################################################
    sFileDir=Base + '/77-Yoke'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    sFileDir=Base + '/77-Yoke/10-Master'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    sFileDir=Base + '/77-Yoke/20-Slave'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    sFileDir=Base + '/77-Yoke/99-SQLite'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    sDatabaseName=Base + '/77-Yoke/99-SQLite/Yoke.db'
    conn = sq.connect(sDatabaseName)
    print('Connecting :',sDatabaseName)
    sSQL='CREATE TABLE IF NOT EXISTS YokeData (\
     PathFileName VARCHAR (1000) NOT NULL\
     );'
    sql.execute(sSQL,conn)
    conn.commit()
    conn.close()   
    return Base,sDatabaseName
################################################################
def makeslavefile(Base,InputFile):
    sExecName=Base + '/77-Yoke/Run-Yoke.py'
    sExecLine='python ' + sExecName + ' ' + InputFile
    os.system(sExecLine)
################################################################
if __name__ == '__main__':
    ################################################################
    print('### Start ############################################')
    ################################################################
    Base,sDatabaseName = prepecosystem()
    connslave = sq.connect(sDatabaseName)
    sSQL="SELECT PathFileName FROM YokeData;"
    SlaveData=pd.read_sql_query(sSQL, connslave)
    for t in range(SlaveData.shape[0]):
        sFile=str(SlaveData['PathFileName'][t])
        print('Spawn:',sFile)
        p = Process(target=makeslavefile, args=(Base,sFile))
        p.start()
        p.join()
    ################################################################
    print('### Done!! ############################################')
    ################################################################