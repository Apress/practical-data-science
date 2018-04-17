################################################################
# -*- coding: utf-8 -*-
################################################################
import networkx as nx
import sys
import os
import sqlite3 as sq
import pandas as pd
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
sDatabaseName=Base + '/01-Vermeulen/00-RawData/SQLite/vermeulen.db'
conn = sq.connect(sDatabaseName)
################################################################
sFileName=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
sOutputFileName='Assess-DAG-Schedule-All.csv'
Company='01-Vermeulen'
################################################################
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
IP_DATA_ALL.index.names = ['RowIDCSV']
IP_DATA_ALL.rename(columns={'Place.Name': 'PlaceName'}, inplace=True)
IP_DATA_ALL.rename(columns={'Post.Code': 'PostCode'}, inplace=True)
#print(IP_DATA_ALL)
print('################')  
sTable='Assess_IP_DATA'
print('Storing :',sDatabaseName,' Table:',sTable)
IP_DATA_ALL.to_sql(sTable, conn, if_exists="replace")
print('################')  

################################################################
G=nx.Graph()
################################################################
print('################')  
sTable = 'Assess_IP_DATA'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.Country,"
sSQL=sSQL+ " A.Country AS NodeName,"
sSQL=sSQL+ " A.Country AS GroupName0,"
sSQL=sSQL+ " 'Country-Router' AS RouterType"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_DATA as A"
sSQL=sSQL+ " ORDER BY A.Country;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):
    sNode=str(CompanyData['NodeName'][i])
    sRouterType=str(CompanyData['RouterType'][i])
    sGroupName0=str(CompanyData['GroupName0'][i])
    G.add_node(sNode,
               routertype=sRouterType,
               group0=sGroupName0)
           
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')

print('################')  
sTable='Assess_IP_Country'
print('Storing :',sDatabaseName,' Table:',sTable)
CompanyData.to_sql(sTable, conn, if_exists="replace")
print('################') 
################################################################
print('################')   
sTable = 'Assess_IP_DATA'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.Country,"
sSQL=sSQL+ " A.PlaceName,"
sSQL=sSQL+ " A.PlaceName || '-' || A.Country AS NodeName,"
sSQL=sSQL+ " A.Country AS GroupName0,"
sSQL=sSQL+ " A.PlaceName AS GroupName1,"
sSQL=sSQL+ " 'Place-Router' AS RouterType"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_DATA as A"
sSQL=sSQL+ " ORDER BY A.Country AND"
sSQL=sSQL+ " A.PlaceName;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):
    sNode=str(CompanyData['NodeName'][i])
    sRouterType=str(CompanyData['RouterType'][i])
    sGroupName0= str(CompanyData['Country'][i])
    sGroupName1= str(CompanyData['PlaceName'][i])
    
    G.add_node(sNode,
               routertype=sRouterType,
               group0=sGroupName0,
               group1=sGroupName1)
           
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')

print('################')  
sTable='Assess_IP_PlaceName'
print('Storing :',sDatabaseName,' Table:',sTable)
CompanyData.to_sql(sTable, conn, if_exists="replace")
print('################') 
################################################################
print('################')   
sTable = 'Assess_IP_DATA'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.Country,"
sSQL=sSQL+ " A.PlaceName,"
sSQL=sSQL+ " A.PostCode,"
sSQL=sSQL+ " A.PlaceName || '-' || A.PostCode || '-' || A.Country AS NodeName,"
sSQL=sSQL+ " A.Country AS GroupName0,"
sSQL=sSQL+ " A.PlaceName AS GroupName1,"
sSQL=sSQL+ " A.PostCode AS GroupName2,"
sSQL=sSQL+ " 'Place-Router' AS RouterType"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_DATA as A"
sSQL=sSQL+ " ORDER BY A.Country AND"
sSQL=sSQL+ " A.PlaceName AND"
sSQL=sSQL+ " A.PostCode;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):
    sNode=str(CompanyData['NodeName'][i])
    sRouterType=str(CompanyData['RouterType'][i])
    sGroupName0= str(CompanyData['GroupName0'][i])
    sGroupName1= str(CompanyData['GroupName1'][i])
    sGroupName2= str(CompanyData['GroupName2'][i])
    
    G.add_node(sNode,
               routertype=sRouterType,
               group0=sGroupName0,
               group1=sGroupName1,
               group2=sGroupName2)
           
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')

print('################')  
sTable='Assess_IP_PostCode'
print('Storing :',sDatabaseName,' Table:',sTable)
CompanyData.to_sql(sTable, conn, if_exists="replace")
print('################') 
################################################################
print('################')   
sTable = 'Assess_IP_DATA'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.Country,"
sSQL=sSQL+ " A.PlaceName,"
sSQL=sSQL+ " A.PostCode,"
sSQL=sSQL+ " A.Latitude,"
sSQL=sSQL+ " A.Longitude,"

sSQL=sSQL+ " (CASE WHEN A.Latitude < 0 THEN "
sSQL=sSQL+ "  'S' || ABS(A.Latitude)"
sSQL=sSQL+ " ELSE "
sSQL=sSQL+ "  'N' || ABS(A.Latitude)"
sSQL=sSQL+ " END ) AS sLatitude,"

sSQL=sSQL+ " (CASE WHEN A.Longitude < 0 THEN "
sSQL=sSQL+ "  'W' || ABS(A.Longitude)"
sSQL=sSQL+ " ELSE "
sSQL=sSQL+ "  'E' || ABS(A.Longitude)"
sSQL=sSQL+ " END ) AS sLongitude"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_DATA as A;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  


sTable='Assess_IP_GPS'
CompanyData.to_sql(sTable, conn, if_exists="replace")
sSQL="select distinct"
sSQL=sSQL+ " A.Country,"
sSQL=sSQL+ " A.PlaceName,"
sSQL=sSQL+ " A.PostCode,"
sSQL=sSQL+ " A.Latitude,"
sSQL=sSQL+ " A.Longitude,"
sSQL=sSQL+ " A.sLatitude,"
sSQL=sSQL+ " A.sLongitude,"
sSQL=sSQL+ " A.sLatitude || '-' || A.sLongitude AS NodeName,"
sSQL=sSQL+ " A.Country AS GroupName0,"
sSQL=sSQL+ " A.PlaceName AS GroupName1,"
sSQL=sSQL+ " A.PostCode AS GroupName2,"
sSQL=sSQL+ " 'GPS-Client' AS RouterType"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_GPS as A"
sSQL=sSQL+ " ORDER BY A.Country AND"
sSQL=sSQL+ " A.PlaceName AND"
sSQL=sSQL+ " A.PostCode AND"
sSQL=sSQL+ " A.Latitude AND"
sSQL=sSQL+ " A.Longitude;"
CompanyData=pd.read_sql_query(sSQL, conn)


for i in range(CompanyData.shape[0]):
    sNode=str(CompanyData['NodeName'][i])
    sRouterType=str(CompanyData['RouterType'][i])
    sGroupName0= str(CompanyData['GroupName0'][i])
    sGroupName1= str(CompanyData['GroupName1'][i])
    sGroupName2= str(CompanyData['GroupName2'][i])
    nLatitude=round(CompanyData['Latitude'][i],6)
    nLongitude=round(CompanyData['Longitude'][i],6) 
    sLatitude= str(CompanyData['sLatitude'][i])
    sLongitude= str(CompanyData['sLongitude'][i])
      
    G.add_node(sNode,
               routertype=sRouterType,
               group0=sGroupName0,
               group1=sGroupName1,
               group2=sGroupName2,
               sLatitude=sLatitude,
               sLongitude=sLongitude,
               nLatitude=nLatitude,
               nLongitude=nLongitude)
           
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')

print('################')  
sTable='Assess_IP_GPS'
print('Storing :',sDatabaseName,' Table:',sTable)
CompanyData.to_sql(sTable, conn, if_exists="replace")
print('################') 
###############################################################
print('################################')
print('Link County to Country')
print('################################')
print('################')  
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.NodeName as N1,"
sSQL=sSQL+ " B.NodeName as N2"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_Country as A,"
sSQL=sSQL+ " Assess_IP_Country as B"
sSQL=sSQL+ " WHERE "
sSQL=sSQL+ " A.Country < B.Country AND "
sSQL=sSQL+ " A.NodeName <> B.NodeName;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):    
    n1= str(CompanyData['N1'][i])    
    n2= str(CompanyData['N2'][i])
    
    print('Link Country :',n1,' to Country :', n2)
    G.add_edge(n1,n2)
print('################################')
            
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################') 
###############################################################
print('################################')
print('Link County to Place')
print('################################')
print('################')  
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.NodeName as N1,"
sSQL=sSQL+ " B.NodeName as N2"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_Country as A,"
sSQL=sSQL+ " Assess_IP_PlaceName as B"
sSQL=sSQL+ " WHERE "
sSQL=sSQL+ " A.Country = B.Country AND "
sSQL=sSQL+ " A.NodeName <> B.NodeName;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):    
    n1= str(CompanyData['N1'][i])    
    n2= str(CompanyData['N2'][i])
    
    print('Link Country :',n1,' to Place : ', n2)
    G.add_edge(n1,n2)
print('################################')
            
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')
###############################################################
print('################################')
print('Link Place to Post Code')
print('################################')
print('################')  
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.NodeName as N1,"
sSQL=sSQL+ " B.NodeName as N2"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_PlaceName as A,"
sSQL=sSQL+ " Assess_IP_PostCode as B"
sSQL=sSQL+ " WHERE "
sSQL=sSQL+ " A.Country = B.Country AND "
sSQL=sSQL+ " A.PlaceName = B.PlaceName AND "
sSQL=sSQL+ " A.NodeName <> B.NodeName;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):    
    n1= str(CompanyData['N1'][i])    
    n2= str(CompanyData['N2'][i])
    
    print('Link Place :',n1,' to Post Code : ', n2)
    G.add_edge(n1,n2)
print('################################')
            
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')
###############################################################
print('################################')
print('Link Post Code to GPS')
print('################################')
print('################')  
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="select distinct"
sSQL=sSQL+ " A.NodeName as N1,"
sSQL=sSQL+ " B.NodeName as N2"
sSQL=sSQL+ " from"
sSQL=sSQL+ " Assess_IP_PostCode as A,"
sSQL=sSQL+ " Assess_IP_GPS as B"
sSQL=sSQL+ " WHERE "
sSQL=sSQL+ " A.Country = B.Country AND "
sSQL=sSQL+ " A.PlaceName = B.PlaceName AND "
sSQL=sSQL+ " A.PostCode = B.PostCode AND "
sSQL=sSQL+ " A.NodeName <> B.NodeName;"
CompanyData=pd.read_sql_query(sSQL, conn)
print('################')  

for i in range(CompanyData.shape[0]):    
    n1= str(CompanyData['N1'][i])    
    n2= str(CompanyData['N2'][i])
    
    print('Link Post Code :',n1,' to GPS : ', n2)
    G.add_edge(n1,n2)
print('################################')
            
print('################################')
print("Nodes of graph: ",nx.number_of_nodes(G))
print("Edges of graph: ",nx.number_of_edges(G))
print('################################')
################################################################
sFileDir=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
sFileName=sFileDir + '/' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
nx.write_gml(G,sFileName)
sFileName=sFileName +'.gz'
nx.write_gml(G,sFileName)
################################################################
################################################################
print('### Done!! ############################################')
################################################################