# Utility Start XML to HORUS =================================
# Standard Tools
#=============================================================
import pandas as pd
import xml.etree.ElementTree as ET
#=============================================================
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root,'entry')
        for index in range(data.shape[1]):
            schild=str(header[index])
            child = ET.SubElement(entry, schild)
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
            entry.append(child)
    result = ET.tostring(root)
    return result
#=============================================================
def xml2df(xml_data):
    root = ET.XML(xml_data) 
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

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

sOutputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.xml'

sXML=df2xml(OutputData)

file_out = open(sOutputFileName, 'wb')
file_out.write(sXML)
file_out.close()

print('CSV to XML - Done')
# Utility done ===============================================