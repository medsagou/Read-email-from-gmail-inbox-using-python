import email
import imaplib
import smtplib
import config

user = config.USER
app_pass = config.APP_PASS

host = config.HOST
port = config.PORT
receiver_email=config.REC_EMAIL
content_dir ="email_content"
def send_email_from_gmail(user=user,app_pass=app_pass, host=host, port = port, subject="Test Email", content_dir=content_dir, email_content="email1.txt"):
    # get email content first
    with open(content_dir +'/'+ email_content, 'r') as F:
        body = F.read()

    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP(host, port) as gmail:
            gmail.starttls()
            gmail.login(user, app_pass)
            gmail.sendmail(user, receiver_email, message)
        print("Email sent successfully!")
        gmail.quit()
    except Exception as error:
        print(f"Error email not send ----> {str(error)}")


send_email_from_gmail()
