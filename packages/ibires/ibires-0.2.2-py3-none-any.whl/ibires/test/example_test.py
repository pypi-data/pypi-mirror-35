import responses
from ibires.core import send
from ibires.simulate import sms_server

def send_messages(messages, connection):
    for to, text in messages.items():
        response = send(to, text, **connection)
        assert response['status']['id'] == 7

@responses.activate
def test_myfun():
    messages = {
                '919999999999': 'Green apples are no oranges',
                '919999999998': 'It is raining now!',
                '919999999997': 'Don\'t forget the homework!'
               }

    # first define connecting options
    # leave this username if you want to simulate only
    connection = {
                  'url': 'https://api.infobip.com/sms/1/text/single',
                  'user': 'Aladdin',
                  'password': 'open sesame',
                  'sender': '919999999999'
                  }

    # this and the @responses.activate decorator simulate
    # the behaviour of https://api.infobip.com/sms/1/text/single
    sms_server(**connection)

    # MAIN CALL
    send_messages(messages, connection)
    
    # here wo don't use any assert statement as such
    # it is sufficient that an error will be raised if
    # we don't get a HTTP 200 response
