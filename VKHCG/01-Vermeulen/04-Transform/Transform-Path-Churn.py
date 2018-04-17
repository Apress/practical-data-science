################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
import networkx as nx
import datetime
pd.options.mode.chained_assignment = None
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
Company='01-Vermeulen'
################################################################
sDataBaseDir=Base + '/' + Company + '/04-Transform/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataBaseDir + '/Vermeulen.db'
conn = sq.connect(sDatabaseName)
################################################################
G=nx.Graph()
################################################################
for M in range(1,10):
    print('Month: ', M)
    MIn = str(M - 1)
    MOut = str(M)
    sFile0 = 'ConnectionsChurn' + MIn + '.csv'
    sFile1 = 'ConnectionsChurn' + MOut + '.csv'
    sTable0 = 'ConnectionsChurn' + MIn 
    sTable1 = 'ConnectionsChurn' + MOut
    
    sFileName0=Base + '/' + Company + '/00-RawData/' + sFile0
    ChurnData0=pd.read_csv(sFileName0,header=0,low_memory=False, encoding="latin-1")
    
    sFileName1=Base + '/' + Company + '/00-RawData/' + sFile1
    ChurnData1=pd.read_csv(sFileName1,header=0,low_memory=False, encoding="latin-1")
    
    ################################################################
    dt1 = datetime.datetime(year=2017, month=1, day=1)
    dt2 = datetime.datetime(year=2017, month=2, day=1)
    ChurnData0['Date'] = dt1.strftime('%Y/%m/%d')
    ChurnData1['Date'] = dt2.strftime('%Y/%m/%d')
    ################################################################
    
    TrackColumns=['SeniorCitizen', 'Partner',
           'Dependents', 'PhoneService', 'MultipleLines',
           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
           'StreamingTV', 'PaperlessBilling', 'StreamingMovies', 'InternetService',
           'Contract', 'PaymentMethod', 'MonthlyCharges']
    ################################################################ 
    for i in range(ChurnData0.shape[0]):
        for TColumn in TrackColumns:
            t=0
            if ChurnData0[TColumn][i] == 'No':
                t+=1
            if t > 4:
                ChurnData0['Churn'][i] = 'Yes'
            else:
                ChurnData0['Churn'][i] = 'No'
    ################################################################ 
    for i in range(ChurnData1.shape[0]):
        for TColumn in TrackColumns:
            t=0
            if ChurnData1[TColumn][i] == 'No':
                t+=1
            if t > 4:
                ChurnData1['Churn'][i] = 'Yes'
            else:
                ChurnData1['Churn'][i] = 'No'
    ################################################################
    print('Store CSV Data')
    ChurnData0.to_csv(sFileName0, index=False)
    ChurnData1.to_csv(sFileName1, index=False)
    ################################################################
    print('Store SQLite Data')
    ChurnData0.to_sql(sTable0, conn, if_exists='replace') 
    ChurnData1.to_sql(sTable1, conn, if_exists='replace') 
    ################################################################                
    for TColumn in TrackColumns:
        for i in range(ChurnData0.shape[0]):
            Node0 = 'Root'
            Node1 = '(' + ChurnData0['customerID'][i] + '-Start)'
            G.add_edge(Node0, Node1)
            Node5 = '(' + ChurnData0['customerID'][i] + '-Stop)'
            G.add_node(Node5)
            
            if ChurnData0['Churn'][i] == 'Yes':                
                NodeA = '(' + ChurnData0['customerID'][i] + '-Start)'
                NodeB = '(' + ChurnData0['customerID'][i] + '-Stop)'  
                if nx.has_path(G, source=NodeA, target=NodeB) == False:
                    NodeC = '(' + ChurnData0['customerID'][i] + '):(Churn)=>(' + ChurnData1['Churn'][i] + ')'
                    G.add_edge(NodeA, NodeC)  
                    G.add_edge(NodeC, NodeB)  
            else:
                if ChurnData0[TColumn][i] != ChurnData1[TColumn][i]:
                    #print(M,ChurnData0['customerID'][i],ChurnData0['Date'][i],ChurnData1['Date'][i],TColumn, ChurnData0[TColumn][i], ChurnData1[TColumn][i])
                    Node2 = '(' + ChurnData0['customerID'][i] + ')-(' + ChurnData0['Date'][i] + ')'
                    G.add_edge(Node1, Node2)
                    Node3 = Node2 + '-(' + TColumn + ')'
                    G.add_edge(Node2, Node3)
                    Node4 = Node3 + ':(' + ChurnData0[TColumn][i] + ')=>(' + ChurnData1[TColumn][i] + ')'
                    G.add_edge(Node3, Node4)
                    
                    if M == 9:
                        Node6 = '(' + ChurnData0['customerID'][i] + '):(Churn)=>(' + ChurnData1['Churn'][i] + ')'
                        G.add_edge(Node4, Node6)  
                        G.add_edge(Node6, Node5)  
                    else:
                        G.add_edge(Node4, Node5)  
                
#for n in G.nodes():
#    print(n)
#    
#for e in G.edges():
#    print(e)
                       
sGraphOutput=Base + '/' + Company + \
    '/04-Transform/01-EDS/02-Python/Transform_ConnectionsChurn_Graph.gml.gz'                          
nx.write_gml(G, sGraphOutput)

sFile0 = 'ConnectionsChurn9.csv'
sFileName0=Base + '/' + Company + '/00-RawData/' + sFile0
ChurnData0=pd.read_csv(sFileName0,header=0,low_memory=False, encoding="latin-1") 
c=0   
for i in range(ChurnData0.shape[0]):
    sCustomer = ChurnData0['customerID'][i]
    NodeX = '(' + ChurnData0['customerID'][i] + '-Start)'
    NodeY = '(' + ChurnData0['customerID'][i] + '-Stop)'  
    if nx.has_path(G, source=NodeX, target=NodeY) == False:
        NodeZ = '(' + ChurnData0['customerID'][i] + '):(Churn)=>(' + ChurnData0['Churn'][i] + ')'
        G.add_edge(NodeX, NodeZ)  
        G.add_edge(NodeZ, NodeX)  
        
    if nx.has_path(G, source=NodeX, target=NodeY) == True:
        pset = nx.all_shortest_paths(G, source=NodeX, target=NodeY, weight=None)
        t=0
        for p in pset:
            t=0
            ps = 'Path: ' + str(p)
            for s in p:
                c+=1
                t+=1
                ts = 'Step: ' + str(t)
                #print(NodeX, NodeY, ps, ts, s)
                if c == 1:
                    pl = [[sCustomer, ps, ts, s]]
                else:
                    pl.append([sCustomer, ps, ts, s])

sFileOutput=Base + '/' + Company + \
    '/04-Transform/01-EDS/02-Python/Transform_ConnectionsChurn.csv'                
df = pd.DataFrame(pl, columns=['Customer', 'Path', 'Step', 'StepName'])
df.index.name = 'RecID'

sTable = 'ConnectionsChurnPaths'
df.to_sql(sTable, conn, if_exists='replace') 
df.to_csv(sFileOutput)
################################################################
print('### Done!! ############################################')
################################################################
            
    