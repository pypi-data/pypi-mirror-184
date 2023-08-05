from email.mime.application import MIMEApplication
import ast
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import configparser
import os


def send_mail(subject, table, to_mail, Attachfile=None, file_directory=None, file_name=None,
              zip_status=None, csv_status=None):
    config = configparser.ConfigParser()
    config.read('config.ini')
    sender_mail = config.get('mail_info', 'sender_email')
    sender_pass = config.get('mail_info', 'sender_password')
    smtp = config.get('mail_info', 'smtp_server')
    cc = ast.literal_eval(config.get('mail_info', 'cc'))
    html = """\
                    <html>
                        <head>
                        <style>
                            table, th, td {
                                border: 1px solid black;
                                border-collapse: collapse;
                            }
                            th, td {
                                padding: 5px;
                                text-align: left;    
                            }    
                        </style>
                        </head>
                    <body>
                    <p>
                    %s
                    </p>
                    </body>
                    </html>
                    """ % table
    html_body = MIMEText(html, 'html')
    # Create the root message and fill in the from, to, and subject headers
    msg = MIMEMultipart('alternative')
    msg.attach(html_body)
    msg['Subject'] = "{}".format(subject)
    msg['From'] = sender_mail
    msg['To'] = ", ".join(to_mail)
    msg['Cc'] = ", ".join(cc)
    if Attachfile == "True":
        for i in range(len(file_directory)):
            file = os.path.basename(file_directory[i])
            if file.endswith(".csv") and csv_status == 0:
                with open(file_directory[i], 'rb') as csvfile:
                    msg.attach(MIMEApplication(csvfile.read(), Name='{}'.format(file_name[i])))
            elif file.endswith(".zip") and zip_status == 0:
                with open("{}".format(file_directory[i]), 'rb') as file:
                    msg.attach(MIMEApplication(file.read(), Name="{}".format(file_name[i])))

    smtp_obj = smtplib.SMTP(smtp)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(sender_mail, sender_pass)
    to_address = to_mail + cc
    smtp_obj.sendmail(sender_mail, to_address, msg.as_string())
    smtp_obj.quit()
