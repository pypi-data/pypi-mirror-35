import pytest

from ibires.core import send
from ibires.simulate import sms_server
import responses
from requests.exceptions import HTTPError

@responses.activate
def test_sms_server_200():
    connection = {
                  'url': 'https://api.infobip.com/sms/1/text/single',
                  'user': 'Aladdin',
                  'password': 'open sesame',
                  'sender': '919999999999'
                 }

    sms_server(**connection)
    response = send(to = '41793026727', text = 'Do not interfere when two blinds discuss colours.', **connection)
    
    assert response['to'] == '41793026727'
    assert len(response['messageId']) == 36
    assert response['smsCount'] == 1
    assert response['status']['description'] == 'Message sent to next instance'
    assert response['status']['groupId'] == 1
    assert response['status']['groupName'] == 'PENDING'
    assert response['status']['id'] == 7
    assert response['status']['name'] == 'PENDING_ENROUTE'

@responses.activate
def test_sms_server_401():
    connection = {
                  'url': 'https://api.infobip.com/sms/1/text/single',
                  'user': 'Aladdin',
                  'password': 'open sesame',
                  'sender': '919999999999'
                 }

    sms_server(**connection)
    with pytest.raises(HTTPError):
        connection['password'] += 'b' # tamper with the password
        response = send(to = '41793026727', text = 'Do not interfere when two blinds discuss colours.', **connection)
