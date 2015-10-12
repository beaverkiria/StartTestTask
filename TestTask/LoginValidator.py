__author__ = 'kirillcherepanov'

import re


def is_login_valid(login):
    if not isinstance(login, basestring):
        raise ValueError('Login must be a string type.')

    p = re.compile(r"""
        (^[a-z]$)              #One symbol login
        |(
        ^[a-z]                 #The first symbol must be a letter
        [a-z,\d,.,-]{0,18}     #Then letters, digits, dots and dashes
        [a-z,\d]$              #The last symbol must be a letter or a digit
        )
    """, re.IGNORECASE | re.VERBOSE)
    m = p.match(login)
    if m:
        return 1
    else:
        return 0

