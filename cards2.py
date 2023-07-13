
#%%
from http.client import HTTPSConnection
from base64 import b64encode
#%%
conn = HTTPSConnection("staging-api.isic.org")
payload = """<?xml version='1.0' encoding='utf-8'?>
        <card>
            <cardNumber>S 507 500 024 953 S</cardNumber>
            <cardType>ISIC</cardType>
            <cardStatus>VALID</cardStatus>
            <printedName>SerracinJaime </printedName>
            <firstName>Jaime </firstName>
            <lastName>Serracin</lastName>
            <dateOfBirth>1994-06-28</dateOfBirth>
            <gender></gender>
            <validFrom>2022-01-01</validFrom>
            <validTo>2022-12-12</validTo>
            <issueType>VIRTUAL_CARD</issueType>
            <institutionName>U del Istmo</institutionName>
            <issuedBy>OTEC</issuedBy>
            <email>jaimeserracin1994@gmail.com</email>
            <customValues>
                <customValue>
                    <key>bloodType</key>
                    <value>O+</value>
                </customValue>
                <customValue>
                    <key>faculty</key>
                    <value>Maest. en Admón Emp ByF</value>
                </customValue>
                <customValue>
                    <key>cedula</key>
                    <value>4-772-1722</value>
                </customValue>
            </customValues>
        </card>"""
user = "panama-test"
password = "'kFm2-n5w39"
headers = {
    "Authorization": "Basic {}".format(
        b64encode(bytes(f"{user}:{password}", "utf-8")).decode("ascii")
    )}
#%%
conn.request("POST", "/ccdb2/rest/1.0/cards", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
