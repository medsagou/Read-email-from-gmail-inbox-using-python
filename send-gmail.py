import email
import imaplib
import smtplib
import config

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

user = config.USER
app_pass = config.APP_PASS

host = config.HOST
port = config.PORT
# receiver_email=config.REC_EMAIL
content_dir ="email_content"

def multi_sender(email_content="email1.txt",
                content_dir=content_dir,
                subject="Join our Google Meet: Introduction to Python by Mohamed Sagou",
                rec_email='rec-email.txt',
                done='done.txt'):


    with open(content_dir + '/' + rec_email,'r') as F:
        emails_lines = F.readlines()
    with open(content_dir + '/' + done, 'r') as F:
        dones = F.read()

    for email_line in emails_lines:
        email = email_line.replace('\n', '')
        email = email.split(',')
        with open(content_dir + '/' + email_content, 'r') as F:
            body = F.read()
        if email[2] in dones:
            continue
        body = body.replace('[R-N]',email[1])
        print(email[2])
        message = f'Subject: {subject}\n\n{body}'
        try:
            with smtplib.SMTP(host, port) as gmail:
                gmail.starttls()
                gmail.login(user, app_pass)
                gmail.sendmail(user, email[2], message)
            print("Email sent successfully!")

            with open(content_dir + '/' + done, 'a') as F:
                F.writelines(email[2])
                F.writelines('\n')
            gmail.quit()
        except Exception as error:
            print(f"Error email not send ----> {str(error)}")
    return

# def send_email_from_gmail(user=user,
#                           app_pass=app_pass, host=host,
#                           port = port,
#                           subject="Test Email",
#                           content_dir=content_dir,
#                           email_content="email1.txt"):
#     # get email content first
#     with open(content_dir +'/'+ email_content, 'r') as F:
#         body = F.read()
#
#     message = f'Subject: {subject}\n\n{body}'
#
#     try:
#         with smtplib.SMTP(host, port) as gmail:
#             gmail.starttls()
#             gmail.login(user, app_pass)
#             gmail.sendmail(user, receiver_email, message)
#         print("Email sent successfully!")
#         gmail.quit()
#     except Exception as error:
#         print(f"Error email not send ----> {str(error)}")


multi_sender()
