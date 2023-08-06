from base64 import b64encode
# for correct doctest order, see http://www.alexandrejoseph.com/blog/2016-03-02-stable-dict-sort-python-doctest.html
from pprint import pprint as _
from requests import post

def send(to, text, url, user, password, sender, timeout = 5):
    """
    Send message text to target number.
    
    :param list|str to: Array of message destination addresses. If you want to send
                        a message to one destination, a single String is supported
                        instead of an Array. Destination addresses must be in
                        international format (Example: '41793026727').
    :param str text: Text of the message that will be sent.
    :param str url: url to post to.
    :param str user: username.
    :param str password: password.
    :param str sender: Represents sender ID and it can be alphanumeric or numeric.
                       Alphanumeric sender ID length should be between 3 and 11 characters (Example: ``'CompanyName'``).
                       Numeric sender ID length should be between 3 and 14 characters.
    :param int timeout: timeout in seconds.
    """
    r = post(url,
             json = {'from': sender, 'to': to, 'text': text},
             headers = make_headers(user, password),
             timeout = timeout
            )
    r.raise_for_status() # fail if re.status_code != 200
    return(r.json()['messages'][0])

def make_headers(user, password):
    """
    Create headers dict.

    :param str user: username.
    :param str password: password.
    """
    auth = b64encode(str.encode(user + ':' + password)).decode()
    headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + auth,
                'Accept': 'application/json'
               }
    return(headers)
