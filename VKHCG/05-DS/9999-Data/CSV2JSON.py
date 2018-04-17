# Utility Start CSV to JSON  =================================
# Standard Tools
#=============================================================
import pandas as pd
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

sOutputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.json'

OutputData.to_json(sOutputFileName,orient='index')

print('CSV to JSON - Done')
# Utility done ===============================================