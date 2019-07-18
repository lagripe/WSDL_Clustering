import math,json,requests
def SimilarityWSDLs(WS1,WS2,coef):
    Attr = MatchWSDLAttributes(WS1,WS2)
    Name = ServiceNameSimilarity(WS1,WS2)
    return coef * (Name + Attr['matchMsg']+Attr['matchPorts']+Attr['matchTypes'])

def MatchWSDLAttributes(WS1,WS2):
    avgMsg= (len(WS1['Messages']) + len(WS2['Messages']))/2
    avgPort=(len(WS1['Ports']) + len(WS2['Ports']))/2
    avgType=(len(WS1['Types']) + len(WS2['Types']))/2
    countMsg = 0
    countTypes=0
    countPorts=0
    for word in WS1['Messages']:
        if word in WS2['Messages']:
            countMsg+=1
    for word in WS1['Ports']:
        if word in WS2['Ports']:
            countPorts+=1
    for word in WS1['Types']:
        if word in WS2['Types']:
            countTypes+=1


    return {'matchMsg':countMsg/avgMsg,
            'matchPorts':countPorts/avgPort,
            'matchTypes':countTypes/avgType
            }
def ServiceNameSimilarity(WS1,WS2):
    count = 0
    total = 0
    for nameWS1 in WS1['Name']:
        for nameWS2 in WS2['Name']:
            total+= NDG(nameWS1,nameWS2)
            count+=1
    try:
        return 1 - (total/count)
    except:
        return 1
def NDG(term1,term2):
    M = 10000000000
    freqx = logResults(term1)
    freqy = logResults(term2)
    if  freqx == float('-inf') or freqy == float('-inf') :
            return 1
    else:
        freqxy = logResults(term1+'+'+term2)
        num = max([freqx, freqy]) - freqxy
        den = math.log10(M) - min([freqx, freqy])
        return num/den
    return None
def logResults(term):
    try:
        return math.log10(int(makeQuerry(term)))
    except:
        return float('-inf')
def makeQuerry(query):
    try:
        req = requests.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyDmmofEyGEd3QGKdbjSRmTfeEdanKiCheE&cx=017576662512468239146:omuauf_lfve&q={}'.format(query))
        res = json.loads(req.content,encoding="UTF-8")
        return int(res['queries']['request'][0]['totalResults'])
    except:
        return -1
