import responses
from ibires.core import send
from ibires.simulate import sms_server

@responses.activate
def test_myfun():
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
    # now, as we have prepared everything, we can shoot our message
    # no user account, no internet connection, no money required
    response = send(to = '919999999998',
                   text = 'Do not interfere when two blinds argue on colours.',
                   **connection)

    # inspect and use response as you desire

    # let's check whether the message has been accepted
    assert response['status']['id'] == 7

    # access other sending report's specifics like
    assert len(response['messageId']) == 36
    assert(response['to']) == '919999999998'
    assert response['status']['description'] == 'Message sent to next instance'
