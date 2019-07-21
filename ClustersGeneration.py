from Parser import PreprocessWSDL
from SimilarityMeasures import SimilarityWSDLs
from os import listdir
import re
import numpy
from py4j.java_gateway import JavaGateway

coef = 0.2
def ClusteringData(dir,coef=0.2):
    directory = listdir(dir)
    lengthDir = len(directory)
    SimilarityMatrix = numpy.zeros((lengthDir,lengthDir),dtype=float)

    for i,_WS in enumerate(directory):

        WS1 = PreprocessWSDL(dir+'\\'+_WS)
        for j  in range(i,lengthDir):

            WS_ = directory[j]
            if i == j : 
                SimilarityMatrix [i,j]  = 0
                continue

            WS_ = directory[j]
            WS2 = PreprocessWSDL(dir+'\\'+WS_)
            # Similarity
            SIM = SimilarityWSDLs(WS1,WS2,coef)
            SimilarityMatrix [i,j]  = SIM
            SimilarityMatrix [j,i]  = SIM
            print(SIM)
            print('---------------------------------------------')
    print(SimilarityMatrix)

    gateway = JavaGateway()
    myClassEntry = gateway.entry_point
    Obj = myClassEntry.Cluster()
'''
import os
directory = listdir('clearedDatabase')
for WS in directory:
    try:WS1 = PreprocessWSDL('clearedDatabase\\'+WS)
    except:
        continue
    if len(WS1['Name']) == 0:continue
    with(open('clearedDatabase\\'+WS,'r')) as f:
        with(open('cleared\\'+WS,'w')) as fnew:
            fnew.write(f.read())

'''

