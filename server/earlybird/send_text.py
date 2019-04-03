from twilio.rest import Client
from os import environ

from .settings import CREDENTIALS


def send_text(recipient, body):
    acct_sid = 'AC032ac56ba28b0ccc0ad81a228093aab3'
    from_number = "+12018176210"

    auth_token = CREDENTIALS['TWILIO_TOKEN']

    client = Client(acct_sid, auth_token)

    message = client.messages.create(
        body=body, from_=from_number, to=recipient)

    if message.error_code:
        raise Exception('Failed to send text. Error code: {}, Error message: {}'.format(
            message.error_code, message.error_message))
