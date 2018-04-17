################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import networkx as nx
import sqlite3 as sq
from pandas.io import sql
import uuid
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
Company='03-Hillman'

InputAssessGraphName='Assess_All_Animals.gml'
EDSAssessDir='02-Assess/01-EDS'
InputAssessDir=EDSAssessDir + '/02-Python'
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
conn1 = sq.connect(sDatabaseName)
################################################################
sDataVaultDir=Base + '/88-DV'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName)
################################################################
sFileName= sFileAssessDir + '/' + InputAssessGraphName
print('################################')
print('Loading Graph :', sFileName)
print('################################')
G=nx.read_gml(sFileName)
print('Nodes: ', G.number_of_nodes())
print('Edges: ', G.number_of_edges())

################################################################
t=0
tMax=G.number_of_nodes()
for node in nx.nodes_iter(G):
    t+=1
    IDNumber=str(uuid.uuid4())
    NodeName=G.node[node]['NodeName']
    print('Extract:',t,' of ',tMax,':',NodeName)
    ObjectLine=[('ObjectBaseKey', ['Species']),
             ('IDNumber', [IDNumber]),
             ('ObjectNumber', [str(t)]),
             ('ObjectValue', [NodeName])] 
    if t==1:
       ObjectFrame = pd.DataFrame.from_items(ObjectLine) 
    else:
        ObjectRow = pd.DataFrame.from_items(ObjectLine)
        ObjectFrame = ObjectFrame.append(ObjectRow) 

################################################################
ObjectHubIndex=ObjectFrame.set_index(['IDNumber'],inplace=False)
################################################################ 
sTable = 'Process-Object-Species'
print('Storing :',sDatabaseName,' Table:',sTable)
ObjectHubIndex.to_sql(sTable, conn1, if_exists="replace")
#################################################################
sTable = 'Hub-Object-Species'
print('Storing :',sDatabaseName,' Table:',sTable)
ObjectHubIndex.to_sql(sTable, conn2, if_exists="replace")
#################################################################
print('################') 
print('Vacuum Databases')
sSQL="VACUUM;"
sql.execute(sSQL,conn1)
sql.execute(sSQL,conn2)
print('################') 
################################################################
print('### Done!! ############################################')
################################################################


#for node1 in nx.nodes_iter(G):
#    p=nx.shortest_path(G, source='world', target=node1, weight=None)
#    print('Path from World to ',node1,':',p)
#
#for node1 in nx.nodes_iter(G):
#    for node2 in nx.nodes_iter(G):
#        p=nx.shortest_path(G, source=node1, target=node1, weight=None)
#        print('Path:',p)
#
#for node1 in nx.nodes_iter(G):
#    for node2 in nx.nodes_iter(G):
#        d=nx.dijkstra_path(G, source=node1, target=node1, weight=None)
#        print('Path:',d)