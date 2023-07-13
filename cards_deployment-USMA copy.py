#%%
from json.tool import main
from tkinter import N
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, date
import pandas as pd

#%%
df_rt = pd.read_csv('data.csv', encoding = 'latin-1')
df_rt['validTo'] = pd.to_datetime(df_rt['validTo'])
df_rt['validTo']=df_rt['validTo'].dt.strftime('%Y-%m-%d')
df_rt['validFrom'] = pd.to_datetime(df_rt['validFrom'])
df_rt['validFrom']=df_rt['validFrom'].dt.strftime('%Y-%m-%d')
df_rt['dateOfBirth'] = pd.to_datetime(df_rt['dateOfBirth'])
df_rt['dateOfBirth']= df_rt['dateOfBirth'].dt.strftime('%Y-%m-%d')
# df_rt['dateOfBirth'] = pd.to_datetime(df_rt['dateOfBirth'])
df_rt['gender']=df_rt['gender'].fillna('')
df_rt['issueType']=df_rt['issueType'].fillna('')
df_rt['issuedOn']=df_rt['issuedOn'].fillna('')
old_df =df_rt
nan_in_col  = df_rt[df_rt['dateOfBirth'].isna()]
df_rt  = df_rt[df_rt['dateOfBirth'].notnull()]
# df_rt = pd.notnull(df_rt["dateOfBirth"])

#%%
df_rt = df_rt.fillna('')
#%%
def data_loader(card):
        url='https://api.isic.org/ccdb2/rest/1.0/cards'
        payload ="""<?xml version='1.0' encoding='utf-8'?>
        <card>
            <cardNumber>"""+card['cardNumber']+"""</cardNumber>
            <cardType>"""+card['cardType']+"""</cardType>
            <cardStatus>"""+card['cardStatus']+"""</cardStatus>
            <printedName>"""+card['printedName']+"""</printedName>
            <firstName>"""+card['firstName']+"""</firstName>
            <lastName>"""+card['lastName']+"""</lastName>
            <dateOfBirth>"""+card['dateOfBirth']+"""</dateOfBirth>
            <gender>"""+card['gender']+"""</gender>
            <validFrom>"""+card['validFrom']+"""</validFrom>
            <validTo>"""+card['validTo']+"""</validTo>
            <issueType>"""+card['issueType']+"""</issueType>
            <institutionName>"""+card['institutionName']+"""</institutionName>
            <issuedBy>OTEC</issuedBy>
            <email>"""+card['email']+"""</email>
            <customValues>
                <customValue>
                    <key>bloodType</key>
                    <value>"""+card['bloodType']+"""</value>
                </customValue>
                <customValue>
                    <key>faculty</key>
                    <value>"""+card['faculty']+"""</value>
                </customValue>
                <customValue>
                    <key>cedula</key>
                    <value>"""+card['cedula']+"""</value>
                </customValue>
            </customValues>
        </card>"""
        print(payload)
        encoded_data = payload.encode('utf-8')
        headers = {'Content-Type': 'application/xml'} # set what your server accepts
        response_post = requests.post(url, headers=headers,
                                auth=HTTPBasicAuth('ccdb-ws-usma-pa','56kfR-29Jm'),
                                data=encoded_data)
        print(response_post.text)
        if (response_post.status_code == 400):
            print(response_post.text)
            return card
        elif(response_post.status_code == 200):
            print(response_post.text)
                

#%%



def main():
    # %%
    df_rt.apply(lambda row: data_loader(row), axis=1)
    #TODO: CATCH ALL FAILED ROWS INTO A DATAFRAME AND RETRY IF THEY FAIL AGAIN GENERATE A CSV AND SAVE IT FOR REFERENCE

# %%


if __name__ == '__main__':
    main()












#%%
#%%
try:
    response = requests.post(
    'https://staging-api.isic.org/ccdb2/rest/1.0/cards',
    auth=HTTPBasicAuth('panama-test', 'kFm2-n5w39'),
    json=data,
    headers=headers
    )
    print(response)
except requests.ConnectionError as error:
    print(error)