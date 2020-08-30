# ---- Strong password ----

# ---- Description ----

# This script uses regular expressions to analyse the strength of a given password.

# ---- Specification ----

# The script needs to execute the following steps:

# 1. Accept, as input, a test password
# 2. Test whether the password is at least 8 characters long
# 3. Test whether the password contains at least one digit
# 4. Test whether the password contains at least one uppercase letter
# 5. Test whether the password contains at least one lowercase letter

# ---- Implementation ----

import re


def test_password(pwd):

    msg = ''

    digit_regex = re.compile(r'\d+')
    upper_regex = re.compile(r'[A-Z]+')
    lower_regex = re.compile(r'[a-z]+')

    if len(pwd) < 8:
        msg = 'Warning: password should be at least 8 characters!'
    elif digit_regex.search(pwd) is None:
        msg = 'Warning: password should contain at least 1 digit!'
    elif upper_regex.search(pwd) is None:
        msg = 'Warning: password should contain at least 1 uppercase character!'
    elif lower_regex.search(pwd) is None:
        msg = 'Warning: password should contain at least 1 lowercase character!'
    else:
        msg = 'Good job! This password choice is sufficiently strong'

    return(msg)


password = input('Please enter a candidate password: ')
test_result = test_password(pwd=password)
print(test_result)
