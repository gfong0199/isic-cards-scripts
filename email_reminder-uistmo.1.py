
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
contador = 400
        
#%%

def send_email(email,fname,card):
    global contador
    # Define the HTML document
    html = '''
        <html>

        <head>
            <meta http-equiv=Content-Type content="text/html; charset=windows-1252">
            <meta name=Generator content="Microsoft Word 15 (filtered)">
            <style>
                <!--
                /* Font Definitions */
                
                @font-face {
                    font-family: "Cambria Math";
                    panose-1: 2 4 5 3 5 4 6 3 2 4;
                }
                
                @font-face {
                    font-family: Calibri;
                    panose-1: 2 15 5 2 2 2 4 3 2 4;
                }
                
                @font-face {
                    font-family: "Agency FB";
                    panose-1: 2 11 5 3 2 2 2 2 2 4;
                }
                /* Style Definitions */
                
                p.MsoNormal,
                li.MsoNormal,
                div.MsoNormal {
                    margin: 0in;
                    font-size: 11.0pt;
                    font-family: "Calibri", sans-serif;
                }
                
                .MsoChpDefault {
                    font-family: "Calibri", sans-serif;
                }
                
                .MsoPapDefault {
                    margin-bottom: 8.0pt;
                    line-height: 107%;
                }
                
                @page WordSection1 {
                    size: 8.5in 11.0in;
                    margin: .5in .5in .5in .5in;
                    border: solid windowtext 1.0pt;
                    padding: 24.0pt 24.0pt 24.0pt 24.0pt;
                }
                
                div.WordSection1 {
                    page: WordSection1;
                }
                
                -->
            </style>

        </head>

        <body lang=EN-US style='word-wrap:break-word'>

            <div class=WordSection1>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'><img width=auto
                    height=78 id="Picture 4"
                    src="cid:image1"
                    alt="Otec Logo"></span><img width=60 height=60 id="Picture 3" src="cid:image2" alt="Isic Logo"></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'><img width=355
                    height=67 id="Picture 6"
                    src="cid:image3" alt="University logo"</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>Estudiante de la
                    Universidad Del ISTMO</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><b><u><span
                    lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
                    color:red;background:white'>Ya activaste tu&nbsp;carné institucional?</span></u></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><u><span
                    lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
                    color:red;background:white'><span style='text-decoration:none'>&nbsp;</span></span></u></b></p>


                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                 <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>Anteriormente hemos enviado a tu correo el número asignado de carné &nbsp;<span
                    style='color:#111111'>que se utilizará para activarlo digitalmente</span></span></p>     

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><b><i><u><span
                    lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
                    color:#111111'>Te estamos reenviando este número&nbsp;para que actives </span></u></i></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><i><u><span
                    lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
                    color:#111111'>tu&nbsp;carné</span></u></i></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><i><span
                    lang=ES-PA style='font-family:"Agency FB",sans-serif;color:#111111'>Si ya lo
                    hiciste, favor hacer caso omiso</span></i></b></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>ESTUDIANTE:</span></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:red'>'''+fname+'''</span></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>TU
                    NÚMERO&nbsp;DE CARNÉ ES:</span></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:16.0pt;font-family:"Agency FB",sans-serif;color:red'>'''+card+'''</span></b></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>Recuerda
                    que, al activar tu carné estudiantil, estas sujeto a<b> multiples </b></span></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>beneficios
                    y descuentos</span></b><span lang=ES-PA style='font-size:18.0pt;font-family:
                    "Agency FB",sans-serif;color:#111111'>!&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:red'>&nbsp;En
                    las siguientes imagenes &nbsp;podras ver los pasos para</span></b></p>

                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:red'>activar
                    tu Carnet estudiantil 2023</span></b></p>
                    <br>
                <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
                    style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:red'>Asistencia por Whatsapp: 6252-9302</span></b></p>

                <p class=MsoNormal><span lang=ES-PA>&nbsp;</span></p>

                <p class=MsoNormal><span lang=ES-PA>&nbsp;</span></p>

                <p class=MsoNormal><span lang=ES-PA>&nbsp;</span></p>

                <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA style='font-family:"Agency FB",sans-serif'><img width=674 height=960
                    src="cid:image4" alt="imagen de ayuda de instalacion" /></span></p>

            </div>

        </body>

        </html>
        '''

    # Set up the email addresses and password. Please replace below with your email address and password
    # email_from = 'gafafong99@gmail.com'
    # password = 'armkdnqeuedbmzhc'
    # email_to = email

    email_from = 'otecpanama@otec.com.pa'
    password = 'julio2019'
    email_to = email
    bcc = ['contactmrwilly@gmail.com','']

    # Generate today's date to be included in the email Subject
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = "U del Istmo <no-reply@otecviajespanama.com>"
    email_message['To'] = email_to
    email_message['Bcc'] = ', '.join(bcc)
    email_message['Subject'] = f'Udi Panamà - '''+card
    # Generate today's date to be included in the email Subject

    # This example assumes the image is in the current directory
    fp = open('Picture1.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    email_message.attach(msgImage)
    # This example assumes the image is in the current directory
    fp = open('Picture2.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image2>')
    email_message.attach(msgImage)
    fp = open('Picture3.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image3>')
    email_message.attach(msgImage)
    # This example assumes the image is in the current directory
    fp = open('Picture4.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image4>')
    email_message.attach(msgImage)


    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    email_message.attach(MIMEText(html, "html"))

    # Convert it as a string
    email_string = email_message.as_string()
    # This example assumes the image is in the current directory

    # Connect to the Gmail SMTP server and Send Email
    context = ssl.create_default_context()

    # print('Mandando Correo--->', email_to)
    # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #     server.login(email_from, password)
    #     server.sendmail(email_from, email_to, email_string)
        
    print('Mandando Correo--->', email_to)
    # try:

    #     with smtplib.SMTP_SSL("mail.otecviajespanama.com", 465, context=context) as server:
    #         server.login(email_from, password)
    #         server.ehlo()
    #         server.sendmail(email_from, email_to, email_string)
    #         server.quit()
    #         print ("Successfully sent email")
    # except smtplib.SMTPException:
    #     print("Error: unable to send email")
    if contador == 0:
        print(contador)
        time.sleep(3600)
        print("Ha pasado una HORA:", date_str)
        contador = 400
        print(contador)
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
        contador = contador - 1
        print(contador)
        with open('emails_sent_istmo.csv', 'a') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
            dict_object.writerow(dict)
      #%%
#%%
#send_email("gafafong99@gmail.com","GUILLERMO, FONG","S 507 000 038 223 J")

#%%
#%%
#send_email("vielka.gomez@otec.com.pa","Gomez, Vielka","445465346546456")
#%%
def main():
    #%%
    df_rt = pd.read_csv('data.csv', encoding='utf-8')
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
    print('empezo', pd.Timestamp.today())
    print('data cargada')

    df_rt.apply(lambda row: send_email(row['email'],row['printedName'],row['cardNumber']), axis=1)

    
#%%
# Call the main function
if __name__ == "__main__":
    main()



#%%
