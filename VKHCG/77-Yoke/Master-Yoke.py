################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import sqlite3 as sq
from pandas.io import sql
import uuid
import re
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
def makemasterfile(sseq,Base,sDatabaseName):
    sFileName=Base + '/77-Yoke/10-Master/File_' + sseq +\
    '_' + str(uuid.uuid4()) + '.txt'
    sFileNamePart=os.path.basename(sFileName)
    smessage="Practical Data Science Yoke \n File: " + sFileName
    with open(sFileName, "w") as txt_file:
        txt_file.write(smessage)
    
    connmerge = sq.connect(sDatabaseName)
    sSQLRaw="INSERT OR REPLACE INTO YokeData(PathFileName)\
            VALUES\
            ('" + sFileNamePart + "');"
    sSQL=re.sub('\s{2,}', ' ', sSQLRaw) 
    sql.execute(sSQL,connmerge)
    connmerge.commit() 
    connmerge.close()        
################################################################
if __name__ == '__main__':
    ################################################################
    print('### Start ############################################')
    ################################################################
    Base,sDatabaseName = prepecosystem()
    for t in range(1,10):
        sFile='{num:06d}'.format(num=t)
        print('Spawn:',sFile)
        p = Process(target=makemasterfile, args=(sFile,Base,sDatabaseName))
        p.start()
        p.join()
    ################################################################
    print('### Done!! ############################################')
    ################################################################