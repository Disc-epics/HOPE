#!/usr/bin/env python3.6.7

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(toaddr, subject, message):

    # Earlybird login Gmail info
    fromaddr = 'earlybirdalertsystem@gmail.com'
    password = 'Earlybird!'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    text = MIMEText(message, 'html')
    msg.attach(text)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except:
        print('Error: could not send email')


def get_subject(status):
    if status is True:
        return "Alert ClientName has been arrested"
    else:
        return "ClientName has been released"


def send_notification(toaddr, worker):
    _html = """\
      <html>
        <body>
          <p>Hi Caseworker name,<br>
            Your ClientName was been release/arrested at date and time. Login to your Account for more detail.<br>
            <a href="https://engineering.purdue.edu/earlybirdsystem">Real Python</a> 
            For more information.
          </p>
        </body>
      </html>
      """
    pass
