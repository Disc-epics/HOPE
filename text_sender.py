import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


# from https://lifehacker.com/how-can-i-send-an-email-via-text-message-5506326
EMAIL_PROVIDER_FORMATS = {
    "Alltel": "{}@message.alltel.com",
    "AT&T": "{}@txt.att.net",  # works
    "T-Mobile": "{}@tmomail.net",  # not working
    "Virgin Mobile": "{}@vmobl.com",
    "Sprint": "{}@messaging.sprintpcs.com",
    "Verizon": "{}@vtext.com",  # works
    "Nextel": "{}@messaging.nextel.com",
    "US Cellular": "{}@mms.uscc.net",
    "Google Fi": "{}@msg.fi.google.com",  # works
    "Metro PCS": "{}@mymetropcs.com",
    "Cricket": "{}@sms.mycricket.com",
    "Boost Mobile": "{}@sms.myboostmobile.com",
    "Mint Mobile": "{}@tmomail.net",
    "Simple Mobile": "{}@smtext.com",
    "C Spire": "{}@cspire1.com",
}

EARLYBIRD_EMAIL = 'earlybirdalertsystem@gmail.com'
EARLYBIRD_FROM = 'Matt Ellenberger <earlybirdalertsystem@gmail.com>'
EARLYBIRD_PW = os.environ['EARLYBIRD_PW']


def supported_carriers():
    return EMAIL_PROVIDER_FORMATS.keys()


def send_text(number, carrier, message):
    try:
        email = EMAIL_PROVIDER_FORMATS[carrier].format(number)
    except KeyError:
        raise "Unknown carrier {}".format(carrier)

    # make an HTML message
    msg = MIMEText(
        '<html><head></head><body>{}</body></html>'.format(message), 'html')
    multi = MIMEMultipart('alternative')
    multi.attach(msg)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
        server.set_debuglevel(1)
        server.login(EARLYBIRD_EMAIL, EARLYBIRD_PW)

        err = server.send_message(
            msg, from_addr=EARLYBIRD_FROM, to_addrs=[email])
        print("Leaving rn")
        for (k, v) in err:
            print("{}: {}", k, v)


if __name__ == "__main__":
    send_text(1234567890, 'T-Mobile', 'Test Message')
