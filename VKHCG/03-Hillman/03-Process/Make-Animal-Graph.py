################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import networkx as nx
import sqlite3 as sq
import numpy as np
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
ReaderCode='SuperDataScientist'
ReaderName='Practical Data Scientist'
################################################################
Company='03-Hillman'
InputRawFileName='Animals.csv'

EDSRetrieveDir='01-Retrieve/01-EDS'
InputRetrieveDir=EDSRetrieveDir + '/02-Python'
InputRetrieveFileName='Retrieve_All_Animals.csv'

EDSAssessDir='02-Assess/01-EDS'
InputAssessDir=EDSAssessDir + '/02-Python'
InputAssessFileName='Assess_All_Animals.csv'
InputAssessGraphName='Assess_All_Animals.gml'
################################################################
sFileRetrieveDir=Base + '/' + Company + '/' + InputRetrieveDir
if not os.path.exists(sFileRetrieveDir):
    os.makedirs(sFileRetrieveDir)
################################################################
sFileAssessDir=Base + '/' + Company + '/' + InputAssessDir
if not os.path.exists(sFileAssessDir):
    os.makedirs(sFileAssessDir)
################################################################
sDataBaseDir=Base + '/' + Company + '/03-Process/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataBaseDir + '/Hillman.db'
conn = sq.connect(sDatabaseName)
################################################################
# Raw to Retrieve
################################################################
sFileName=Base + '/' + Company + '/00-RawData/' + InputRawFileName
print('###########')
print('Loading :',sFileName)
AnimalRaw=pd.read_csv(sFileName,header=0,low_memory=False, encoding = "ISO-8859-1")
AnimalRetrieve=AnimalRaw.copy()
print(AnimalRetrieve.shape)
################################################################
sFileName=sFileRetrieveDir + '/' + InputRetrieveFileName
print('###########')
print('Storing Retrieve :',sFileName)
AnimalRetrieve.to_csv(sFileName, index = False)
################################################################
# Retrieve to Assess
################################################################
AnimalGood1 = AnimalRetrieve.fillna('0', inplace=False)
AnimalGood2=AnimalGood1[AnimalGood1.ItemName!=0]
AnimalGood2[['ItemID','ParentID']]=AnimalGood2[['ItemID','ParentID']].astype(np.int32)

AnimalAssess=AnimalGood2
print(AnimalAssess.shape)
################################################################
sFileName=sFileAssessDir + '/' + InputAssessFileName
print('###########')
print('Storing Assess :',sFileName)
AnimalAssess.to_csv(sFileName, index = False)
################################################################
print('################')  
sTable='All_Animals'
print('Storing :',sDatabaseName,' Table:',sTable)
AnimalAssess.to_sql(sTable, conn, if_exists="replace")
print('################')  
################################################################

print('################')  
sTable='All_Animals'
print('Loading Nodes :',sDatabaseName,' Table:',sTable)
sSQL=" SELECT DISTINCT"
sSQL=sSQL+ " CAST(ItemName AS VARCHAR(200)) AS NodeName,"
sSQL=sSQL+ " CAST(ItemLevel AS INT) AS NodeLevel"
sSQL=sSQL+ " FROM"
sSQL=sSQL+ " " + sTable + ";"

AnimalNodeData=pd.read_sql_query(sSQL, conn)

print(AnimalNodeData.shape)
################################################################
print('################')  
sTable='All_Animals'
print('Loading Edges :',sDatabaseName,' Table:',sTable)
sSQL=" SELECT DISTINCT"
sSQL=sSQL+ " CAST(A1.ItemName AS VARCHAR(200)) AS Node1,"
sSQL=sSQL+ " CAST(A2.ItemName AS VARCHAR(200)) AS Node2"
sSQL=sSQL+ " FROM"
sSQL=sSQL+ " " + sTable + " AS A1"
sSQL=sSQL+ " JOIN"
sSQL=sSQL+ " " + sTable + " AS A2"
sSQL=sSQL+ " ON"
sSQL=sSQL+ " A1.ItemID=A2.ParentID;"

AnimalEdgeData=pd.read_sql_query(sSQL, conn)
print(AnimalEdgeData.shape)
################################################################
G=nx.Graph()
t=0
G.add_node('world', NodeName='World')
################################################################
GraphData=AnimalNodeData
print(GraphData)
################################################################
m=GraphData.shape[0]
for i in range(m):
    t+=1
    sNode0Name=str(GraphData['NodeName'][i]).strip()
    print('Node :',t,' of ',m,sNode0Name)
    sNode0=sNode0Name.replace(' ', '-').lower()
    G.add_node(sNode0, NodeName=sNode0Name)
    if GraphData['NodeLevel'][i] == 0:
        G.add_edge(sNode0,'world')         
################################################################
GraphData=AnimalEdgeData
t=0
################################################################
m=GraphData.shape[0]

for i in range(m):
    t+=1
    sNode0Name=str(GraphData['Node1'][i]).strip()
    sNode1Name=str(GraphData['Node2'][i]).strip()
    print('Link :',t,' of ',m,sNode0Name,' to ',sNode1Name)
    sNode0=sNode0Name.replace(' ', '-').lower()
    sNode1=sNode1Name.replace(' ', '-').lower()
    G.add_edge(sNode0,sNode1)
################################################################
RCode=ReaderCode.replace(' ', '-').lower()
G.add_node(RCode,NodeName=ReaderName)  
G.add_edge('homo-sapiens',RCode)
################################################################
sFileName= sFileAssessDir + '/' + InputAssessGraphName
print('################################')
print('Storing :', sFileName)
print('################################')
nx.write_gml(G,sFileName)
sFileName=sFileName +'.gz'
nx.write_gml(G,sFileName)
################################################################
# Find Lists of Objects
################################################################
TargetNodes=[ReaderCode,'Andre Vermeulen','Angus', 'Tigger', 'Chris Hillman']
for j in range(len(TargetNodes))  :
    TargetNodes[j]=TargetNodes[j].replace(' ', '-').lower()
################################################################    
for TargetNode in TargetNodes:
    if TargetNode in nx.nodes(G):
        print('=============================')
        print('Path:','World',' to ',G.node[TargetNode]['NodeName'])
        print('=============================')
        for nodecode in nx.shortest_path(G,source='world',target=TargetNode):
            print(G.node[nodecode]['NodeName'])        
        print('=============================')
    else:
        print('=============================')
        print('No data - ', TargetNode, ' is missing!')
        print('=============================')           
################################################################ 
print('=============================')
print(' How do we turn Angus into Tigger?')
print('=============================')
for nodecode in nx.shortest_path(G,source='angus',target='tigger'):
    print(G.node[nodecode]['NodeName']) 
################################################################   
print('=============================')  
print('How do you make Chris a Doctor?')
print('=============================')     
for nodecode in nx.shortest_path(G,source='chris-hillman',target='dr-chris'):
    print(G.node[nodecode]['NodeName'])       
print('=============================')    
################################################################
print('### Done!! ############################################')
################################################################