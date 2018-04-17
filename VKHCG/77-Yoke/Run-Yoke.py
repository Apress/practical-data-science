################################################################
# -*- coding: utf-8 -*-
################################################################
import sys
import os
import shutil
################################################################
def prepecosystem():
    if sys.platform == 'linux': 
        Base=os.path.expanduser('~') + '/VKHCG'
    else:
        Base='C:/VKHCG'
    ############################################################
    sFileDir=Base + '/77-Yoke'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    sFileDir=Base + '/77-Yoke/10-Master'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    sFileDir=Base + '/77-Yoke/20-Slave'
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    ############################################################
    return Base
################################################################
def makeslavefile(Base,InputFile):
    sFileNameIn=Base + '/77-Yoke/10-Master/'+InputFile
    sFileNameOut=Base + '/77-Yoke/20-Slave/'+InputFile
    
    if os.path.isfile(sFileNameIn):
        shutil.move(sFileNameIn,sFileNameOut)
################################################################
if __name__ == '__main__':
    ################################################################
    print('### Start ############################################')
    ################################################################
    Base = prepecosystem()
    sFiles=list(sys.argv)
    for sFile in sFiles:
        if sFile != 'Run-Yoke.py':
            print(sFile)
            makeslavefile(Base,sFile)
    ################################################################
    print('### Done!! ############################################')
    ################################################################