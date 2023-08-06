from ibires.core import make_headers

def test_make_headers():
    assert make_headers('Aladdin', 'open sesame') ==  { 'Accept': 'application/json',
                                                        'Authorization': 'Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==',
                                                        'Content-Type': 'application/json' }
