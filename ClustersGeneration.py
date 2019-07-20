from Parser import PreprocessWSDL
from SimilarityMeasures import SimilarityWSDLs
from os import listdir
import re
import numpy
from py4j.java_gateway import JavaGateway


coef = 0.2
def ClusteringData(dir,coef=0.2):
    directory = listdir(dir)
    SimilarityMatrix = {}

    for i in range(0,len(directory)):

        _WS = directory[i]
        WS1 = PreprocessWSDL(dir+'\\'+_WS)

        if len(WS1['Name']) == 0:continue
        SimilarityMatrix[_WS] = []
        for j in range(0,len(directory)):

            if i > j:continue
            if i == j : 
                SimilarityMatrix[_WS].append(0)
                continue

            WS_ = directory[j]
            WS2 = PreprocessWSDL(dir+'\\'+WS_)
            
            if len(WS2['Name']) == 0:continue

            # Similarity
            
            SIM = SimilarityWSDLs(WS1,WS2,coef)
            SimilarityMatrix[_WS].append(SIM)
            print(SIM)
            
            print('---------------------------------------------')
    print(SimilarityMatrix)

    gateway = JavaGateway()
    myClassEntry = gateway.entry_point
    Obj = myClassEntry.Cluster()
'''
import os
for WS in directory:
    try:WS1 = PreprocessWSDL('qws-wsdls\\'+WS)
    except:
        continue
    with(open('qws-wsdls\\'+WS,'r')) as f:
        with(open('clearedDatabase\\'+WS,'w')) as fnew:
            fnew.write(f.read())
'''
