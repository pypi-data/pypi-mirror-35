import responses
import json

from ibires.core import make_headers
from ibires.reports import gen_accepted

def sms_server(url, user, password, sender):
    """
    Function to mock infobip's single messaging interface.

    :param str url: url to post to.
    :param str user: username.
    :param str password: password.
    :param str sender: Represents sender ID and it can be alphanumeric or numeric.
                       Alphanumeric sender ID length should be between 3 and 11 characters (Example: ``'CompanyName'``).
                       Numeric sender ID length should be between 3 and 14 characters.
    """
    def request_callback(request):
        payload = json.loads(request.body.decode())
        print(request.headers)
        headers_should_be = make_headers(user, password)
        headers_is = request.headers
        headers_valid = 'Content-Type' in headers_is and 'Authorization' in headers_is and 'Accept' in headers_is
        if headers_valid:
            auth_valid = headers_is['Authorization'] == headers_should_be['Authorization']
        if headers_valid and auth_valid:
            return(200, request.headers, json.dumps(gen_accepted(payload['to'])))
        elif headers_valid:
            return(401, {}, None)
        else:
            return(403, {}, None)

    responses.add_callback(
        responses.POST, url,
        callback = request_callback,
        content_type = 'application/json',
    )
