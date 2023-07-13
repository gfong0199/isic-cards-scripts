# Import modules

#%%
from email.mime.application import MIMEApplication
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd
# %%
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the message
    email_message.attach(file_attachment)
#%%
# Define the HTML document
html = '''
    <html>
   
        <head>
        <meta http-equiv=Content-Type content="text/html; charset=windows-1252">
        <meta name=Generator content="Microsoft Word 15 (filtered)">
        <style>
        <!--
        /* Font Definitions */
        @font-face
            {font-family:"Cambria Math";
            panose-1:2 4 5 3 5 4 6 3 2 4;}
        @font-face
            {font-family:Calibri;
            panose-1:2 15 5 2 2 2 4 3 2 4;}
        @font-face
            {font-family:"Agency FB";
            panose-1:2 11 5 3 2 2 2 2 2 4;}
        /* Style Definitions */
        p.MsoNormal, li.MsoNormal, div.MsoNormal
            {margin:0in;
            font-size:11.0pt;
            font-family:"Calibri",sans-serif;}
        .MsoChpDefault
            {font-family:"Calibri",sans-serif;}
        .MsoPapDefault
            {margin-bottom:8.0pt;
            line-height:107%;}
        @page WordSection1
            {size:8.5in 11.0in;
            margin:.5in .5in .5in .5in;
            border:solid windowtext 1.0pt;
            padding:24.0pt 24.0pt 24.0pt 24.0pt;}
        div.WordSection1
            {page:WordSection1;}
        -->
        </style>

        </head>

        <body lang=EN-US style='word-wrap:break-word'>

        <div class=WordSection1>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'><img width=193
        height=78 id="Picture 4"
        src="'''+imag+'''"
        alt="Logo, company name&#10;&#10;Description automatically generated"></span><img
        width=87 height=87 id="Picture 3"
        src="./Picture1.png"
        alt="Ver las imagenes de origen"></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'><img width=239
        height=57 id="Picture 6"
        src="cambiar imagen"></span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>Estudiante de la
        Universidad Del ISTMO</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><b><u><span
        lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
        color:red;background:white'>Ya activaste tu&nbsp;carné institucional?</span></u></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><u><span
        lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
        color:red;background:white'><span style='text-decoration:none'>&nbsp;</span></span></u></b></p>

        <p class=MsoNormal align=center style='text-align:center'><i><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:black;
        background:white'>Sigue las instrucciones</span></i></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>Desde Enero del
        2022, hemos estado enviando a tu correo un número&nbsp;de&nbsp;<span
        style='color:#111111'>carné, </span></span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>el
        cual se te solicitaba para activar tu&nbsp;carné.&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><b><i><u><span
        lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
        color:#111111'>Te estamos reenviando este número&nbsp;para que actives </span></u></i></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><i><u><span
        lang=ES-PA style='font-size:18.0pt;font-family:"Agency FB",sans-serif;
        color:#111111'>tu&nbsp;carné</span></u></i></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><i><span
        lang=ES-PA style='font-family:"Agency FB",sans-serif;color:#111111'>Si ya lo
        hiciste, favor hacer caso omiso</span></i></b></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>ESTUDIANTE:</span></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:black'>___________________________________</span></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>TU
        NÚMERO&nbsp;DE CARNÉ ES:</span></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:16.0pt;font-family:"Agency FB",sans-serif;color:black'>_____________________________________________________________________________________________________________________</span></b></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>Recuerda
        que, al activar tu carné estudiantil, estas sujeto a<b> multiples </b></span></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:#111111'>beneficios
        y descuentos</span></b><span lang=ES-PA style='font-size:18.0pt;font-family:
        "Agency FB",sans-serif;color:#111111'>!&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif'>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:red'>&nbsp;En
        las siguientes imagenes &nbsp;podras ver los pasos para</span></b></p>

        <p class=MsoNormal align=center style='text-align:center'><b><span lang=ES-PA
        style='font-size:18.0pt;font-family:"Agency FB",sans-serif;color:red'>activar
        tu Carnet estudiantil 2022</span></b></p>

        <p class=MsoNormal><span lang=ES-PA>&nbsp;</span></p>

        <p class=MsoNormal><span lang=ES-PA>&nbsp;</span></p>

        <p class=MsoNormal><span lang=ES-PA>&nbsp;</span></p>

        <p class=MsoNormal align=center style='text-align:center'><span lang=ES-PA
        style='font-family:"Agency FB",sans-serif'><img width=674 height=960
        src="imagen"></span></p>

        </div>

        </body>
    </html>
    '''

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'gafafong99@gmail.com'
password = 'armkdnqeuedbmzhc'
email_to = 'gafafong99@gmail.com'

# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))
# Convert it as a string
email_string = email_message.as_string()
# This example assumes the image is in the current directory
fp = open('Picture1.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
email_message.attach(msgImage)
attach_file_to_email(email_message, 'Picture1.png')
# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()

#%%
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)