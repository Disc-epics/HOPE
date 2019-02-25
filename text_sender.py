from twilio.rest import Client
from os import environ

acct_sid = 'AC032ac56ba28b0ccc0ad81a228093aab3'
auth_token = environ['TWILLO_TOKEN']

if __name__ == '__main__':
    client = Client(acct_sid, auth_token)

    message = client.messages.create(
        body="Earlybird!", from_="+12018176210", to="+17204818810")
