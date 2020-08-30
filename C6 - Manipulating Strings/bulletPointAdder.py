#!/usr/local/bin/python3.8
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

text_as_list = text.split('\n')
for i in range(len(text_as_list)):
    text_as_list[i] = '* ' + text_as_list[i]

text = '\n'.join(text_as_list)

pyperclip.copy(text)
