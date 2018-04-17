################################################################
# -*- coding: utf-8 -*-
################################################################
import os
import pandas as pd
################################################################
InputFileName1='Incoterm_2010.csv'
InputFileName2='GB_Postcode_Warehouse.csv'
InputFileName3='GB_Postcodes_Shops.csv'
OutputFileName='Retrieve_Incoterm_RuleSet.csv'
Company='03-Hillman'
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
### Import Incoterms
################################################################
sFileName1=Base + '/' + Company + '/00-RawData/' + InputFileName1
print('###########')
print('Loading :',sFileName1)
IncotermGrid=pd.read_csv(sFileName1,header=0,low_memory=False)
sColumns=[]
for i in range(1,IncotermGrid.shape[1]):
    oldColumn=IncotermGrid.columns[i]
    newColumn=str(i)+'-'+ oldColumn
    IncotermGrid.rename(columns={oldColumn: newColumn}, inplace=True)
    sColumns.append(newColumn)
print(sColumns)
print('Rows :',IncotermGrid.shape[0])
print('Columns :',IncotermGrid.shape[1])
print('###########')

################################################################
### Import Warehouse
################################################################
sFileName2=Base + '/' + Company + '/00-RawData/' + InputFileName2
print('###########')
print('Loading :',sFileName2)
Warehouse=pd.read_csv(sFileName2,header=0,low_memory=False)
print('Rows :',Warehouse.shape[0])
print('Columns :',Warehouse.shape[1])
print('###########')
################################################################
### Import Shops
################################################################
sFileName3=Base + '/' + Company + '/00-RawData/' + InputFileName3
print('###########')
print('Loading :',sFileName3)
Shop=pd.read_csv(sFileName3,header=0,low_memory=False)
print('Rows :',Shop.shape[0])
print('Columns :',Shop.shape[1])
print('###########')
################################################################
sFileDir=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
### Feature Extract Incoterms
################################################################
#sColumns=['Seller','Carrier','Port_From','Ship',
#          'Port_To','Terminal','Named_Place','Buyer']

IncotermRule = pd.melt(
        IncotermGrid,
        id_vars='Shipping_Term',
        value_vars=sColumns,
        var_name='Step_Name', 
        value_name='Party_Name')
print('###########')
print('Melting - Incoterm Grid')
print('Rows :',IncotermRule.shape[0])
print('Columns :',IncotermRule.shape[1])
print('###########')

IncotermRule['Step_Order']=IncotermRule.apply(lambda row:
            row['Step_Name'][:1]
            ,axis=1)
IncotermRule['Step']=IncotermRule.apply(lambda row:
            row['Step_Name'][2:]
            ,axis=1)
IncotermRule.drop('Step_Name', axis=1, inplace=True)

#print(IncotermRule)
################################################################
t1=IncotermRule[IncotermRule.Party_Name =='Seller']
t1.insert(4, 'Seller_Duty', 1)
t1.insert(5, 'Seller_Insurance', 1)
t1.insert(6, 'Seller_Carry', 1)
t1.insert(7, 'Buyer_Duty', 0)
t1.insert(8, 'Buyer_Insurance', 0)
t1.insert(9, 'Buyer_Carry', 0)
################################################################
IncotermRuleSet=t1
################################################################
t2=IncotermRule[IncotermRule.Party_Name =='Buyer']
t2.insert(4, 'Seller_Duty', 0)
t2.insert(5, 'Seller_Insurance', 0)
t2.insert(6, 'Seller_Carry', 0)
t2.insert(7, 'Buyer_Duty', 1)
t2.insert(8, 'Buyer_Insurance', 1)
t2.insert(9, 'Buyer_Carry', 1)
################################################################
IncotermRuleSet=IncotermRuleSet.append(t2, ignore_index=True)
################################################################
t3=IncotermRule[IncotermRule.Party_Name =='Insurance']
t3.insert(4, 'Seller_Duty', 1)
t3.insert(5, 'Seller_Insurance', 0)
t3.insert(6, 'Seller_Carry', 1)
t3.insert(7, 'Buyer_Duty', 0)
t3.insert(8, 'Buyer_Insurance', 1)
t3.insert(9, 'Buyer_Carry', 0)
###############################################################
IncotermRuleSet=IncotermRuleSet.append(t3, ignore_index=True)
################################################################
IncotermRuleSet.drop('Party_Name', axis=1, inplace=True)
################################################################
IncotermRuleSetSort = IncotermRuleSet.sort_values(
            ['Shipping_Term','Step_Order'], 
            ascending=[1, 1]
        )
print(IncotermRuleSetSort)
################################################################

sFileName2=sFileDir + '/' + OutputFileName
IncotermRuleSetSort.to_csv(sFileName2, index = False)

################################################################
print('### Done!! ############################################')
################################################################