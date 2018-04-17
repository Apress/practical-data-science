
################################################################
import sys
import os
import xml.etree.ElementTree as ET
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
Company= '02-Krennwallner'
sFileDir=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
XMLFileName='Retrieve_Online_Visitor.xml'
sFileName=sFileDir + '/' + XMLFileName 
################################################################
xml_data = open(sFileName).read() 
root = ET.XML(xml_data)
for i, child in enumerate(root):
    record = {}
    for subchild in child:
        record[subchild.tag] = subchild.text
    print(record)
################################################################