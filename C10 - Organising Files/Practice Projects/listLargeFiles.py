#!/usr/bin/env python
# listLargeFiles.py - walks through a given folder tree and lists files above a certain minimum size

import os
import sys
import pyinputplus as pyip


def list_large_files(search_dir, min_size):

    if not os.path.exists(search_dir):
        print('Error: the provided file path does not exist')
        sys.exit()

    for folder, subfolders, filenames in os.walk(search_dir):

        for filename in filenames:
            abs_path = os.path.join(search_dir, folder, filename)
            file_size = os.path.getsize(abs_path)
            # Since the user-defined input is measured in MB we multiply the following argument by 1,000,000
            if file_size >= 1000000 * int(min_size):
                print(
                    f'Large file located: "{filename}" (Size: {int(file_size / 1000000)} MB) stored at "{abs_path}"')


search_dir_input = pyip.inputStr('Please enter an absolute path to search: ')
min_size_input = pyip.inputInt('Please enter a minimum file size (MB): ')

list_large_files(search_dir_input, min_size_input)
