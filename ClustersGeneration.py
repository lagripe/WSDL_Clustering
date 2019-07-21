from Parser import PreprocessWSDL
from SimilarityMeasures import SimilarityWSDLs
from os import listdir
import re
import numpy
from py4j.java_gateway import JavaGateway,GatewayParameters
import sys,array

def Cluster(dir,coef=0.2):
    gateway = JavaGateway()
    Entry = gateway.entry_point
    SimilarityMatrix = GenerateMatrix(dir,coef)
    print(QTCluster(SimilarityMatrix,Entry))

def GenerateMatrix(dir,coef=0.2):
    
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
    return SimilarityMatrix
    
def QTCluster(matrix,Entry):
    header = array.array('i', list(matrix.shape))
    body = array.array('f', matrix.flatten().tolist())
    if sys.byteorder != 'big':
        header.byteswap()
        body.byteswap()
    buf = bytearray(header.tostring() + body.tostring())
    return Entry.ParseMatrix(buf)

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

