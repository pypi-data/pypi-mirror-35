import random
import arrow
from json import loads, dumps
from time import time
from uuid import uuid4

from ibires.codes import hsis, status_group, status_id, error_group, error_id

"""
    A set to generate status on message posting and final delivery report
    for infobip's SMS API, namely:
      o gen_accepted: Report on message posting.
      o gen_dlr: Final delivery report.
"""

def gen_accepted(to = '919999999999', text = None, error = False):
    """
    Returns accepted response (when SMS is posted).
    
    :param list|str to: Array of message destination addresses. If you want to send
                        a message to one destination, a single String is supported
                        instead of an Array. Destination addresses must be in
                        international format (Example: 41793026727).
    :param str text: Text of the message that will be sent.
    :param bool error: True if a random error should happen.
    """

    result = {'messages': []}
    if isinstance(to, str):
        result['messages'].append({'to': to, 'status': dict(status_id[7]), 'smsCount': sms_parts(text), 'messageId': gen_msgid()})
    else:
        for no in to:
            result['messages'].append({'to': to, 'status': dict(status_id[7]), 'smsCount': sms_parts(text), 'messageId': gen_msgid()})
        result['bulkId'] = gen_msgid()
    for no in result['messages']:
        no['status'].update(id=7)
        if 'action' in no['status'].keys():
            no['status'].pop('action')
    return(result)

def gen_dlr(to = '919999999999', text = None, delivered = True, time = None, bulkId = False, country_code = None):
    """
    Returns final delivery report.
    
    :param str to: target number.
    :param bool delivered: True if dlr should tell that message has been delivered.
    :param int time: Timestamp as epoch of sentAt and doneAt of dlr.
                     Default of None effects ``arrow.now()``.
    :param bool bulkId: Has the message been posted to multiple recipients?
    :param int country_code: country_code to restrict random mccMnc choice to.
    """
    if not time:
        time = arrow.now()
    result = {}
    result['results'] = [{}]
    if bulkId:
        result['results'][0]['bulkId'] = gen_msgid()
    result['results'][0]['mccMnc'] = gen_mccMnc(country_code)
    result['results'][0]['messageId'] = gen_msgid()
    result['results'][0]['to'] = str(to)
    result['results'][0]['sentAt'] = str(time.format('YYYY-MM-DD hh:mm:ss.SSSZ'))
    result['results'][0]['doneAt'] = str(time.format('YYYY-MM-DD hh:mm:ss.SSSZ'))
    result['results'][0]['smsCount'] = sms_parts(text)
    result['results'][0]['price'] = {'pricePerMessage': 0.01, 'currency': 'EUR'}
    result['results'][0]['status'] = gen_status(delivered)
    result['results'][0]['error'] = gen_error(delivered)
    return(result)

def gen_msgid():
    """
    Returns msgid which is UUID.
    """
    #return(str(time()).replace('.', ''))
    return(str(uuid4()))

def gen_status(delivered = True):
    """
    Returns status of message.

    :param delivered: True if status should indicate that message has been delivered.
    """
    result = {}
    keys = list(status_id.keys())
    if delivered:
        valid = [3]
    else:
        valid = [2,4,5]
    while result == {} or result['groupId'] not in valid:
        result['id'] = random.choice(keys)
        result.update(dict(status_id[result['id']]))
    result.pop('action')
    return(result)

def gen_error(delivered = True):
    """
    Generate error report.
    
    :param gen_error: True if error should indicate that message has been delivered.
    """
    result = {}
    if delivered:
        valid = [0]
    else:
        valid = [1,2,3]
    # 5000, 5001 is call: not SMS
    while result == {} or result['groupId'] not in valid or result['id'] in [5000,5001]:
        id_keys = list(error_id.keys())
        group_keys = list(error_group.keys())
        result['id'] = random.choice(id_keys)
        result.update(dict(error_id[result['id']]))
        result.update(dict(error_group[result['groupId']]))
    return(result)

def strip_report(report, json = False):
    """
    Get the bare delivery report.
    
    :param report: the delivery report as json or dict.
    :param bool json: True if output should be json else dict is returned.
    """
    if not isinstance(report, dict):
        report = loads(report)
    if 'results' in report.keys():
        report = report['results'][0]
    elif 'messages' in report.keys():
        report = report['messages'][0]
    if json:
        return(report)
    else:
        return(dumps(report))

def sms_parts(text):
    """
    Determine message parts.
    """
    if text is None:
        l = 0
    else:
        l = len(text)
    if l == 0:
        return(1)
    else:
        parts = int(l / 160)
        if l % 160 > 0:
            parts += 1
        return(parts)

def gen_mccMnc(country_code = None):
    """
    Return random mccMnc that is HNI.
    HNI = 'MCC' + 'MNC'
    IMSI = 'HNI' + 'MSIN'
    MCC is Mobile Country Code.
    MNC is Mobile Network Code.
    MSIN is Mobile Subscriber Identity Number.
    IMSI is Integrated Mobile Subscriber Identity.
    
    :param int country_code: to restrict selection to.
    """

    if country_code:
        ccs = list(filter(lambda x: 'country_code' in x, hsis))
        sel = list(filter(lambda x: 'country_code' in x and 'active' in x and x['active'] and x['mnc'] and x['country_code'] == country_code, ccs))
    else:        
        sel = list(filter(lambda x: 'active' in x and x['active'] and x['mnc'], hsis))

    if len(sel) > 0:
        row = random.choice(sel)
        return(str(row['mcc']) + str(row['mnc']))
    else:
        return(None)

