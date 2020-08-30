#!/usr/local/bin/python3.8

# ---- Phone and email extractor script ----

# ---- Description ----

# This script allows you to find all of the phone numbers and email addresses contained within a long web page or document.

# ---- Process flow ----

# Roughly speaking, the process is as follows:

# 1. Use the 'pyperclip' module to copy and paste strings
# 2. Create two regexes, one for matching the phone numbers and the other for matching the email addresses
# 3. Find *all* matches, not just the first match, for each regex
# 4. Neatly format the matched strings into a single string that can be pasted
# 5. Display some kind of message if no matches were found in the text

# ---- Code ----

import pyperclip  # for copy and paste functionality
import re  # for regex functionality

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
# note that the findall() method returns a tuple equal to the length of the groups plus 1
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    # if there is an extension...
    if groups[8] != '':
        phone_number += ' ex.' + groups[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
