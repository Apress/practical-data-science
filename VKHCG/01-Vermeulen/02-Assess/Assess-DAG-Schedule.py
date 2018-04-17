################################################################
import networkx as nx
import sys
import os
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
sInputFileName='01-Retrieve/01-EDS/01-R/Retrieve_IP_DATA_CORE.csv'
sOutputFileName='Assess-DAG-Schedule.gml'
Company='01-Vermeulen'
################################################################
### Import Core Company Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
CompanyRawData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
CompanyData=CompanyRawData.drop_duplicates(subset=None, keep='first', inplace=False)
print('Loaded Company :',CompanyData.columns.values)
print('################################')
################################################################
print(CompanyData)
print('################################')
print('Rows : ',CompanyData.shape[0])
print('################################')
################################################################
G=nx.Graph()
################################################################
for i in range(CompanyData.shape[0]):    
    sGroupName0= str(CompanyData['Country'][i])
    sGroupName1= str(CompanyData['Place.Name'][i])
    sGroupName2= str(CompanyData['Post.Code'][i])
    nLatitude=round(CompanyData['Latitude'][i],6)
    nLongitude=round(CompanyData['Longitude'][i],6)  
    
    CountryName=sGroupName0
    print('Add Country Node :',sGroupName0)
    G.add_node(CountryName,
               routertype='CountryName',
               group0=sGroupName0)
    
    sPlaceName= sGroupName1 + '-' + sGroupName0
    G.add_node(sPlaceName,
               routertype='PlaceName',
               group0=sGroupName0,
               group1=sGroupName1)
    
    sPostCodeName= sGroupName1 + '-' + sGroupName2  + '-' + sGroupName0
    print('Add Post Code Node :',sPostCodeName)
    G.add_node(sPostCodeName,
               routertype='PostCode',
               group0=sGroupName0,
               group1=sGroupName1,
               group2=sGroupName2)
  
    if nLatitude < 0:
        sLatitude = 'S-' + str(abs(nLatitude))
    else:
        sLatitude = 'N-' + str(abs(nLatitude))   
        
    if nLongitude < 0:
        sLongitude = 'W-' + str(abs(nLongitude))
    else:
        sLongitude = 'E-' + str(abs(nLongitude))     
        
    sGPS= sLatitude + '-' + sLongitude
    print('Add GPS Node :',sGPS)
    G.add_node(sGPS,routertype='GPS',
               group0=sGroupName0,
               group1=sGroupName1,
               group2=sGroupName2,
               sLatitude=sLatitude,
               sLongitude=sLongitude,
               nLatitude=nLatitude,
               nLongitude=nLongitude)
################################################################
print('################################')
print('Link County to Country')
print('################################')
for n1 in nx.nodes_iter(G):
    if G.node[n1]['routertype'] == 'CountryName':
        for n2 in nx.nodes_iter(G):
            if G.node[n2]['routertype'] == 'CountryName':
                if n1 != n2:
                    print('Link :',n1,' to ', n2)
                    G.add_edge(n1,n2)
print('################################')

print('################################')
print('Link County to Place')
print('################################')
for n1 in nx.nodes_iter(G):
    if G.node[n1]['routertype'] == 'CountryName':
        for n2 in nx.nodes_iter(G):
            if G.node[n2]['routertype'] == 'PlaceName':
                if G.node[n1]['group0'] == G.node[n2]['group0']:
                    if n1 != n2:
                        print('Link :',n1,' to ', n2)
                        G.add_edge(n1,n2)
print('################################')

print('################################')
print('Link Place to Post Code')
print('################################')
for n1 in nx.nodes_iter(G):
    if G.node[n1]['routertype'] == 'PlaceName':
        for n2 in nx.nodes_iter(G):
            if G.node[n2]['routertype'] == 'PostCode':
                if G.node[n1]['group0'] == G.node[n2]['group0']:                    
                    if G.node[n1]['group1'] == G.node[n2]['group1']:
                        if n1 != n2:
                            print('Link :',n1,' to ', n2)
                            G.add_edge(n1,n2)
print('################################')


print('################################')
print('Link Post Code to GPS')
print('################################')
for n1 in nx.nodes_iter(G):
    if G.node[n1]['routertype'] == 'PostCode':
        for n2 in nx.nodes_iter(G):
            if G.node[n2]['routertype'] == 'GPS':
                if G.node[n1]['group0'] == G.node[n2]['group0']:                    
                    if G.node[n1]['group1'] == G.node[n2]['group1']:                 
                        if G.node[n1]['group2'] == G.node[n2]['group2']:
                            if n1 != n2:
                                print('Link :',n1,' to ', n2)
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