from Parser import PreprocessWSDL
from SimilarityMeasures import SimilarityWSDLs
from os import listdir
import re
coef = 0.2

for i,_WS in enumerate(listdir('qws-wsdls')):
    try:WS1 = PreprocessWSDL('qws-wsdls\\'+_WS)
    except:continue
    if len(WS1['Name']) == 0:continue
    print(WS1['Name'])
    for j,WS_ in enumerate(listdir('qws-wsdls')):
        if i == j:
            continue
        try:WS2 = PreprocessWSDL('qws-wsdls\\'+ WS_)
        except:continue
        if len(WS2['Name']) == 0:continue
        print(WS2['Name'])
        
        # Similarity
        print(SimilarityWSDLs(WS1,WS2,coef))
        print('---------------------------------------------')
