from ibires.reports import strip_report, gen_msgid, gen_accepted, gen_status, gen_error, gen_dlr
from ibires.reports import status_id, status_group, error_id, error_group, gen_mccMnc, sms_parts

import pytest
import arrow

strip_report_data = [ gen_accepted(), gen_dlr(delivered = False), gen_dlr(delivered = True) ]

@pytest.mark.parametrize('report', strip_report_data)
def test_strip_report(report):
    assert 'status' in strip_report(report, json = True).keys()
    assert 'status' in strip_report(report)

def test_gen_msgid():
    assert len(gen_msgid()) in [36]

gen_accepted_data = [
                        ['919999999998', 'The quick brown fox jumps over the lazy dog.'],
                        [['919999999998', '919999999999'], 'The quick brown fox jumps over the lazy dog.']
                    ]

@pytest.mark.parametrize('to, text', gen_accepted_data)
def test_gen_accepted(to, text):
    report = gen_accepted(to, text)
    for no in report['messages']:
        assert no['smsCount'] == 1
        assert no['status'] == {'groupId': 1, 'id': 7, 'name': 'PENDING_ENROUTE', 'description': 'Message sent to next instance', 'groupName': 'PENDING'}
        assert 'action' not in no['status']
        assert no['to'] == to

gen_status_data = [ True, False ]

@pytest.mark.parametrize('delivered', gen_status_data)
def test_gen_status(delivered):
    status = gen_status(delivered = delivered)
    print(status)
    if delivered:
        assert status['groupId'] == 3 and status['groupId'] in list(status_group.keys())
    else:
        assert status['id'] != 5 and status['id'] in list(status_id.keys())
        assert status['groupId'] in [0,1,2,4,5] and status['id'] in list(status_id.keys())

gen_error_data = [ True, False ]

@pytest.mark.parametrize('delivered', gen_error_data)
def test_gen_error(delivered):
    response = gen_error(delivered)
    print(response)
    assert response['id'] not in [5000,5001] # no call
    if delivered:
        assert response['groupId'] == 0 and response['id'] in list(error_id.keys())

    else:
        assert response['id'] != 0 and response['id'] in list(error_id.keys())
        assert response['groupId'] != 0 and response['groupId'] in list(error_group.keys())

gen_dlr_data = [ [True, True],
                 [True, False],
                 [False, True],
                 [False, False]
               ]

@pytest.mark.parametrize('delivered, bulkId', gen_dlr_data)
def test_gen_dlr(delivered, bulkId):
    to = '919999999998'
    result = gen_dlr(to, delivered = delivered, bulkId = bulkId)
    if bulkId:
        assert len(result['results'][0]['bulkId']) == 36
    assert arrow.get(result['results'][0]['sentAt']).datetime.date() == arrow.now().datetime.date()
    assert arrow.get(result['results'][0]['doneAt']).datetime.date() == arrow.now().datetime.date()
    assert result['results'][0]['to'] == to
    assert result['results'][0]['smsCount'] == 1
    assert len(result['results'][0]['mccMnc']) > 3
    assert result['results'][0]['price'] == {'pricePerMessage': 0.01, 'currency': 'EUR'}
    assert result['results'][0]['status']['id'] in list(status_id.keys())
    assert result['results'][0]['error']['id'] in list(error_id.keys())
    assert result['results'][0]['error']['id'] not in [5000,5001] # no call
    
    if delivered:
        valid_status_group = [3]
        valid_error_group = [0]
    else:
        valid_status_group = [2,4,5]
        valid_error_group = [1,2,3]
    assert result['results'][0]['status']['groupId'] in valid_status_group
    assert result['results'][0]['error']['groupId'] in valid_error_group


def test_sms_parts():
    assert sms_parts('') ==  1
    assert sms_parts('The quick brown fox jumps over the lazy dog.') == 1
    assert sms_parts('The quick brown fox jumps over the lazy dog. \
        The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. \
        The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.') == 2

def test_gen_mccMnc():
    mm = gen_mccMnc(91)
    assert mm[0:3] == '404'


