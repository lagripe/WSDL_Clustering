import operator
import re
from zeep import Client
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords as st
import zeep.wsdl.wsdl as parser
def getCamelFormat(sentence):
        return re.findall(r'[A-Z]+[a-z]+',re.sub(r'.*?}','', str(sentence).strip())) +  re.findall(r'^[a-z]+',re.sub(r'.*?}','', str(sentence).strip()))


def PreprocessWSDL(wsdl):
        client = Client(wsdl=wsdl)
        output = []
        # Get Service Name
        for service in client.wsdl.services.values():
                ServiceName = ' '.join(re.findall(r'[A-Z]+[a-z]+',service.name))
        portTypes = []
        # Get PortTypes
        for port in client.wsdl.port_types.values():
                portTypes = portTypes + getCamelFormat(port.name)
                
                operations = sorted(
                port.operations.values(),
                key=operator.attrgetter('name'))
                for operation in operations:
                        # Operation
                        portTypes = portTypes + getCamelFormat(operation.name)
                        # Input
                        portTypes = portTypes + getCamelFormat(operation.input_message.name)
                        # Output
                        portTypes = portTypes + getCamelFormat(operation.output_message.name)
                        
        Messages =[]      
        # GET Messages
        for msg in client.wsdl.messages.values():
                Messages = Messages + getCamelFormat(msg.name)
                

        complexTypes= []
        # GET Types 
        for element in client.wsdl.types.types:
                if str(element.signature).__contains__('Complex'):
                        complexTypes = complexTypes + getCamelFormat(element.name)
        for element in client.wsdl.types.elements:
                if str(element.signature).__contains__('Complex'):
                        complexTypes = complexTypes + getCamelFormat(element.name)

        # GET documentation
        documentation = ''
        with open(wsdl,'r') as wsd :
                doc = wsd.read()
                doc = re.sub(r'[\t\n]',' ',doc)
                documentation = ' '.join(re.findall(r'<\w+:documentation\s*.*?>(.*?)</\w+:documentation>',doc))
        # Clear Documentation
        documentation = re.sub(r'[^a-zA-Z\s]',' ',documentation)
        documentation = re.sub(r'\s+',' ',documentation)
        documentation = documentation.strip()
        documentation = documentation.split(' ')

        for word in documentation:
                splittedWord = re.findall(r'[A-Z][a-z]+',word)        
                if len(splittedWord) > 1:
                        output = output + splittedWord
                else:
                        output.append(word)
        # stop words Eliminate
        Lemmatizer = WordNetLemmatizer()
        stopwords = list(st.words('english')) + ["in", "no", "soap", "http", "post", "get", "update", "servers", "of", "response", "to", "string",'out','as','set','type','request','requests','is','they','are','it','href','the','an','or','and','nor','has','for','a','https','if','else','on','web','service']
        ServiceName = [Lemmatizer.lemmatize(str(entity).lower(),pos='v') for entity in ServiceName.split(' ') if str(entity).lower() not in stopwords and len(str(entity).lower()) > 2 ]
        portTypes = [Lemmatizer.lemmatize(str(entity).lower(),pos='v') for entity in portTypes if str(entity).lower() not in stopwords and len(str(entity).lower()) > 2 ]
        complexTypes = [Lemmatizer.lemmatize(str(entity).lower(),pos='v') for entity in complexTypes if str(entity).lower() not in stopwords and len(str(entity).lower()) > 2]
        Messages = [Lemmatizer.lemmatize(str(entity).lower(),pos='v') for entity in Messages if str(entity).lower() not in stopwords and len(str(entity).lower()) > 2]
        output = [Lemmatizer.lemmatize(str(entity).lower(),pos='v') for entity in output if str(entity).lower() not in stopwords and len(str(entity).lower()) > 2]
        print (ServiceName)
        return {'Name':list(set(ServiceName)),
                'Messages':list(set(Messages)),
                'Types':list(set(complexTypes)),
                'Ports':list(set(portTypes)),
                'Documentations':list(set(output))
                }



# -------- Steem or Lemmatize words ??---------------
