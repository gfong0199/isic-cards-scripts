
#%%
from cgi import print_arguments
from email.mime.application import MIMEApplication
from email.utils import make_msgid
from glob import glob
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.image import MIMEImage
import time
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd
import csv


lista_util =pd.DataFrame()
 # list of column names 
        
field_names = ['Emails','Status']

        
#%%

def send_email(email, u):
    global contador
    # Define the HTML document
    html = '''
        Data Subida a '''+u+'''
        '''

    # Set up the email addresses and password. Please replace below with your email address and password
    # email_from = 'gafafong99@gmail.com'
    # password = 'armkdnqeuedbmzhc'
    # email_to = email

    email_from = 'ventaspanama@otec.com.pa'
    password = 'julio2019'
    email_to = email
    bcc = ['gafafong99@gmail.com','']

    # Generate today's date to be included in the email Subject
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = "U del Istmo <no-reply@otecviajespanama.com>"
    email_message['To'] = email_to
    email_message['Bcc'] = ', '.join(bcc)
    email_message['Subject'] = f'Udi Panamà - '''
    # Generate today's date to be included in the email Subject

    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    email_message.attach(MIMEText(html, "html"))

    # Convert it as a string
    email_string = email_message.as_string()
    # This example assumes the image is in the current directory


    print('Mandando Correo--->', email_to)
    try:    
        server = smtplib.SMTP_SSL("mail.otecviajespanama.com", 465)  
        #stmplib docs recommend calling ehlo() before & after starttls()  
        server.ehlo()  
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string) 
        server.close()  
    # Display an error message if something goes wrong.  
    except Exception as e:  
        print ("Error: ", e)  
        print(email_to)
        lista_util=pd.DataFrame({"Emails":[email_to],"Status":['Failed']})
        print(lista_util)
        dict = {"Emails":email_to, "Status":"Fallido"}
        contador = contador - 1
        with open('emails_fallido_istmo.csv', 'a') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
            dict_object.writerow(dict)
      

    else:  
        print ("Email sent!")
        lista_util=pd.DataFrame({"Emails":[email_to],"Status":['Enviado']})
        print(lista_util)
        dict = {"Emails":email_to, "Status":"Enviado"}
        with open('emails_sent_istmo.csv', 'a') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
            dict_object.writerow(dict)
      
