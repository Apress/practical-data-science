# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
import re
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
sInputFileName='03-Process/01-EDS/02-Python/Process_ExchangeRates.csv'
################################################################
sOutputFileName='05-Organise/01-EDS/02-Python/Organise-Forex.csv'
Company='04-Clark'
################################################################
sDatabaseName=Base + '/' + Company + '/05-Organise/SQLite/clark.db'
conn = sq.connect(sDatabaseName)
#conn = sq.connect(':memory:')
################################################################
################################################################
### Import Forex Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
ForexDataRaw=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('################################')
################################################################
ForexDataRaw.index.names = ['RowID']
sTable='Forex_All'
print('Storing :',sDatabaseName,' Table:',sTable)
ForexDataRaw.to_sql(sTable, conn, if_exists="replace")
################################################################
sSQL="SELECT 1 as Bag\
       , CAST(min(Date) AS VARCHAR(10)) as Date \
       ,CAST(1000000.0000000 as NUMERIC(12,4)) as Money \
       ,'USD' as Currency \
       FROM Forex_All \
       ;"
sSQL=re.sub("\s\s+", " ", sSQL)
nMoney=pd.read_sql_query(sSQL, conn)

################################################################
nMoney.index.names = ['RowID']
sTable='MoneyData'
print('Storing :',sDatabaseName,' Table:',sTable)
nMoney.to_sql(sTable, conn, if_exists="replace")
################################################################
sTable='TransactionData'
print('Storing :',sDatabaseName,' Table:',sTable)
nMoney.to_sql(sTable, conn, if_exists="replace")
################################################################
ForexDay=pd.read_sql_query("SELECT Date FROM Forex_All GROUP BY Date;", conn)
################################################################
t=0
for i in range(ForexDay.shape[0]):
    sDay=ForexDay['Date'][i]
    sSQL='\
    SELECT M.Bag as Bag, \
           F.Date as Date, \
           round(M.Money * F.Rate,6) AS Money, \
           F.CodeIn AS PCurrency, \
           F.CodeOut AS Currency \
    FROM MoneyData AS M \
    JOIN \
    ( \
        SELECT \
        CodeIn, CodeOut, Date, Rate \
        FROM \
        Forex_All \
        WHERE\
        CodeIn = "USD" AND CodeOut = "GBP" \
        UNION \
        SELECT \
        CodeOut AS CodeIn, CodeIn AS CodeOut,  Date, (1/Rate) AS Rate \
        FROM \
        Forex_All \
        WHERE\
        CodeIn = "USD" AND CodeOut = "GBP" \
    ) AS F \
    ON \
    M.Currency=F.CodeIn \
    AND \
    F.Date ="' + sDay + '";'
    sSQL=re.sub("\s\s+", " ", sSQL)
    
    ForexDayRate=pd.read_sql_query(sSQL, conn)
    for j in range(ForexDayRate.shape[0]):
        sBag=str(ForexDayRate['Bag'][j])
        nMoney=str(round(ForexDayRate['Money'][j],2))
        sCodeIn=ForexDayRate['PCurrency'][j]
        sCodeOut=ForexDayRate['Currency'][j]
    
    sSQL='UPDATE MoneyData SET Date= "' + sDay + '", '
    sSQL= sSQL + ' Money = ' + nMoney + ', Currency="' + sCodeOut + '"'
    sSQL= sSQL + ' WHERE Bag=' + sBag + ' AND Currency="' + sCodeIn + '";'
    
    sSQL=re.sub("\s\s+", " ", sSQL)
    cur = conn.cursor()
    cur.execute(sSQL)
    conn.commit()
    t+=1
    print('Trade :', t, sDay, sCodeOut, nMoney)
    
    sSQL=' \
    INSERT INTO TransactionData ( \
                                RowID, \
                                Bag, \
                                Date, \
                                Money, \
                                Currency \
                            )  \
    SELECT ' + str(t) + ' AS RowID, \
       Bag, \
       Date, \
       Money, \
       Currency \
    FROM MoneyData \
    ;'
    
    sSQL=re.sub("\s\s+", " ", sSQL)
    
    cur = conn.cursor()
    cur.execute(sSQL)
    conn.commit()
################################################################
sSQL="SELECT RowID, Bag, Date, Money, Currency FROM TransactionData ORDER BY RowID;"
sSQL=re.sub("\s\s+", " ", sSQL)
TransactionData=pd.read_sql_query(sSQL, conn)

OutputFile=Base + '/' + Company + '/' + sOutputFileName
TransactionData.to_csv(OutputFile, index = False)
################################################################