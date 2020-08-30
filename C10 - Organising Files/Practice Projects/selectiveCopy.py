#!/usr/bin/env python
# selectiveCopy.py - walks through a given folder tree and searches for files with a certain file extension

import os
import sys
import re
import shutil


def selective_copy(search_dir, extension, new_sub_dir):
    print('---- PROGRESS LOG ----')

    # Compile a regular expression to use for matching files with the user-supplied extension
    regex = re.compile(extension + '$')

    # Collate all files within the 'search_dir' which match the user-defined 'extension' string

    # If the user-defined directory to be searched does not exist, then the script will exit execution
    if not os.path.exists(search_dir):
        if not search_dir.startswith('/'):
            print('Error: the user-supplied directory to search does not exist. Did you miss a leading "/"?')
        else:
            print('Error: the user-supplied directory to search does not exist!')
        sys.exit()

    print(f'Stage 1: searching "{search_dir}" for files with the extension "{extension}"...')

    # Create a new subfolder to house matching files by referring to the user-defined 'new_dir' string
    print(f'Stage 2: creating new subdirectory, "{new_sub_dir}", to store matched files...')
    new_dir = os.path.join(search_dir, new_sub_dir)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    # Copy all of the matching files into the new directory
    print(
        f'Stage 3: copying relevant files to new subdirectory, "{new_sub_dir}"...\n---- COPY LOG ----')
    for filename in os.listdir(search_dir):
        mo = regex.search(filename)
        if mo is None:
            continue
        else:
            print(f'Copying "{filename}" to "{new_sub_dir}"')
            shutil.copy(os.path.join(search_dir, filename), new_dir)

    print('---- PROCESS COMPLETE ----')


selective_copy('/Users/Johnny/Desktop/Images', '.jpg', 'JPGs')
selective_copy('/Users/Johnny/Desktop/Images', '.png', 'PNGs')
