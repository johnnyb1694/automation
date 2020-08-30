#! python
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import shutil  # for shell functionality (i.e. renaming files)
import os  # for the purpose of listing files in a current directory
import re  # for regular expressions

# Create a regex that matches files with the american date format
date_pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d{2})
    (.*?)$
    """, re.VERBOSE)

# Loop over the files in the current (symbolised by the '.' notation) working directory.
for american_filename in os.listdir('.'):
    mo = date_pattern.search(american_filename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename (see instructions online for a thorough grouping explanation)
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename.
    european_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths (for the purpose of utilising the 'move()' method from 'shutil')
    abs_wd = os.path.abspath('.')
    american_filename = os.path.join(abs_wd, american_filename)
    european_filename = os.path.join(abs_wd, european_filename)

    # Rename the files.
    print(f'Renaming "{american_filename}" to "{european_filename}"...')
    shutil.move(american_filename, european_filename)
