import zeep
from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep import xsd
header = xsd.Element(
           '{http://drm.webservices.epm.oracle}AppParameters',
                    xsd.ComplexType([
                        xsd.Element('{http://drm.webservices.epm.oracle}serverUrl',xsd.String()),
						xsd.Element('{http://drm.webservices.epm.oracle}sessionParams',xsd.String()),
                    ])
                )
header_value = header(serverUrl='http://localhost:5240/oracle/drm/apiadapter',sessionParams='ProductVersion=11.1.2,CultureName=en-US,TimeZoneOffset=-360')
client = Client(wsdl='http://localhost:9000/oracle-epm-drm-webservices/DrmService?wsdl', wsse=UsernameToken('drmws', '********'))
response = client.service.getSysPrefs(_soapheaders=[header_value])
dict_fndWildcard=response[0]
print('Print test response: For ',dict_fndWildcard['name'])
print('Descr:',dict_fndWildcard['descr'])
print('Value:',dict_fndWildcard['value'])
for j in range(66) : 
        print(response[j])
