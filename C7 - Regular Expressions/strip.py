# ---- Strong password ----

# ---- Description ----

# This script contains a function which attempts to replicate the 'strip()' method.

# ---- Implementation ----

import re


def strip_spaces(txt):

    strip_regex = re.compile(r'^(\s*)(.+\w)(\s*)$')
    strip_mo = strip_regex.search(txt)

    # Note: the second group, signified by '2', relates to the '(.+\w)' part of the regex!
    body = strip_mo.group(2)

    return(body)


sample_text = input("Please enter an 'unstripped' version of text: ")
stripped_text = strip_spaces(sample_text)
print("Text successfully stripped:\n" + stripped_text)
