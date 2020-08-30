# ---- Regex search ----

# ---- Description ----

# This program opens all .txt files within a given folder and then searches for any line which matches a user-supplied regular expression.

# ---- Specification ----

# This program needs to:
# 1. ALlow the user to specify a relative path to the folder containing the text files which need to be analysed
# 2. Allow the user to specify a regular expression to search for
# 3. For each file:
#   (i) Read each separate line; and
#   (ii) Establish which line (if any) matches the user-supplied regular expression

# ---- Implementation ----

import re
import os
from pathlib import Path


def get_matching_lines(txt, regex):

    txt_contents = open(txt)
    txt_lines = txt_contents.readlines()
    matching_lines = []
    for n in range(len(txt_lines)):
        if regex.search(txt_lines[n]) is not None:
            matching_lines.append(n)

    return(matching_lines)


input_dir = input('Please specify the directory where your text files are located: ')
input_regex = input(
    'Please specify which regular expression you want to search for: ')  # e.g. 'hello'

r = re.compile(input_regex)
t = re.compile(r'.txt$')

dir_files = os.listdir(Path(input_dir))
txt_files = [f for f in dir_files if r.match(f)]

for f in txt_files:
    p = Path(input_dir) / f
    matching_lines = get_matching_lines(p, r)
    print(f'The file {f} has matches for the input regex on the following lines: {matching_lines}')
