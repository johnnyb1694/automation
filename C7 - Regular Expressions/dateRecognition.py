# ---- Date recognition ----

# ---- Description ----

# This script allows you to detect and validate any series of dates in the DD/MM/YYYY format.

# ---- High level specification ----

# The script needs to execute the following steps:

# 1. It needs to acquire a passage of text for analysis
# 2. It then needs to extract any dates which match the DD/MM/YYYY format
# 3. Subsequently, it must validate each date iteratively

# ---- Low level specification ----

# In order to fulfil the requirements laid out above, we probably need to implement the following:

# 1. Acquire text by 'pasting' text we have manually copied to a global variable via the 'pyperclip' library
# 2. Create a regular expression which is able to capture and return dates of the DD/MM/YYYY format in a given passage
# 3. Create a series of tests inside a loop which are able to validate non-sensical months (e.g. '14') and leap years
# 4. Print a log of results

# ---- Implementation ----

import pyperclip
import re

# 1. Acquire text via the 'paste()' method in pyperclip
text = pyperclip.paste()

# 2. Create a regular expression to return all dates that are in the DD/MM/YYYY format
ddmmyyyy_regex = re.compile(r'(\d{2})\/(\d{2})\/(\d{4})')
ddmmyyyy_matches = ddmmyyyy_regex.findall(text)  # note that this will return a list of tuples

# 3. Create a series of tests inside a loop which are able to validate each date in turn ('d' stands for date)

# Note: we set up a list variable to log the results of the script
log = []

for match in ddmmyyyy_matches:

    # Note: 'd' refers to a given tuple (where each group is day, month and year respectively)
    # Thus, the following selectors extract each respective element of the tuple as a string
    d = match[0]
    m = match[1]
    y = match[2]

    ddmmyyyy_as_string = '/'.join([d, m, y])

    if int(m) not in range(1, 13):
        msg = 'The following match has an invalid number of months: ' + ddmmyyyy_as_string
        log.append(msg)
    elif int(m) in [4, 6, 9, 11]:
        if int(d) > 30:
            msg = 'The following match has an invalid number of days for this month: ' + ddmmyyyy_as_string
            log.append(msg)
        else:
            msg = 'The following match is valid: ' + ddmmyyyy_as_string
            log.append(msg)
    elif int(m) in [1, 3, 5, 7, 8, 10, 12]:
        if int(d) > 31:
            msg = 'The following match has an invalid number of days for this month: ' + ddmmyyyy_as_string
            log.append(msg)
        else:
            msg = 'The following match is valid: ' + ddmmyyyy_as_string
            log.append(msg)
    else:
        if (int(d) == 29):
            if ((int(y) % 4 == 0) and (int(y) % 100 == 0) and (int(y) % 400 != 0)) or (int(y) % 4 != 0):
                msg = 'The following match relates to an invalid leap year: ' + ddmmyyyy_as_string
                log.append(msg)
            else:
                msg = 'The following match is valid: ' + ddmmyyyy_as_string
                log.append(msg)
        elif (int(d) > 29):
            msg = 'The following match has an invalid number of days for this month: ' + ddmmyyyy_as_string
            log.append(msg)
        else:
            msg = 'The following match is valid: ' + ddmmyyyy_as_string
            log.append(msg)

print('---- Date recognition script ----\nThe results of the script are as follows:\n')
for l in log:
    print(l)
