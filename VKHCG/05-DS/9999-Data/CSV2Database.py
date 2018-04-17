# Utility Start CSV to SQLite Database  ======================
# Standard Tools
#=============================================================
import pandas as pd
import sqlite3 as sq
#=============================================================
# Input Agreement ============================================
#=============================================================
sInputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData=pd.read_csv(sInputFileName,encoding="latin-1")
print('Input Data Values ===================================')
print(InputData)
print('=====================================================')
#=============================================================
# Processing Rules ===========================================
#=============================================================
ProcessData=InputData
print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')
#=============================================================
# Output Agreement ===========================================
#=============================================================
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/utility.db'
sOutputTable='Country_Code'
conn = sq.connect(sOutputFileName)
OutputData.to_sql(sOutputTable, conn, if_exists="replace")
print('CSV to Database - Done')
# Utility done ===============================================