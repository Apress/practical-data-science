# -*- coding: utf-8 -*-
################################################################
import sys
import os
import pandas as pd
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
sFileName=Base + '/01-Vermeulen/00-RawData/StudentData.csv'
################################################################

#Calc
#gpa,gre,rank,admit

#df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")
t=0
nS=1
tMax=0
for GPALoop in range(10,45,nS):
    for QR in range(130,171,nS):
        for VR in range(130,171,nS):
            tMax+=1
            
for GPALoop in range(10,45,nS):
    GPA = int(GPALoop/10)
    GPA2 = round(GPALoop/10,2)
    #Quantitative.Reasoning
    for QR in range(130,171,nS):
        #Verbal.Reasoning
        for VR in range(130,171,nS):
            c1=(-2080.74559330863+(VR*6.38369593312407)+(QR*10.6230921641945))
            c2=int(c1)
            if c2 < 200:
                c3=200
            else:
                c3=c2
                
            if c3 > 800:
                c4=800
            else:
                c4=c3
                        
            if(VR+QR) > 259:
                GRE=int(c4)
            else:
                GRE=int(0)
                
            c5=(-109.493972390779+(VR*0.911896551285247))
            
            if c5 > 0:
                c6=round(c5,0)
            else:
                c6=0
            VerbalScore=int(c6)
            
            c7=(-158.418743409747+(QR*1.24338698204798))
            
            if c7 > 0:
                c8=round(c7,0)
            else:
                c8=0
            QuantitativeScore=int(c8)
            
            nRank=int(GPA)
            
            if QR > 160 and VR > 160 and nRank>1:
                nAdmit=1
            else:
                nAdmit=0
            
            t+=1
            StudentName='C'+ format(t, '06d')
            
            StudentLine=[('name', [StudentName]),
                         ('gpa', [GPA]),
                         ('gre', [GRE]),
                         ('rank', [nRank]),
                         ('admit', [nAdmit]),
                         ('qr', [QR]),
                         ('vr', [VR]),
                         ('gpareal', [GPA])
                         ] 
            StudentRow= pd.DataFrame.from_items(StudentLine)
            print(t,' of ', tMax)
            #print(StudentRow)
            if t==1:
                StudentFrame=StudentRow
            else:
                StudentFrame=StudentFrame.append(StudentRow)
################################################################
print (StudentFrame.shape)
StudentFrame.to_csv(sFileName, index = False, encoding="latin-1")
################################################################
print('### Done!! ############################################')
################################################################