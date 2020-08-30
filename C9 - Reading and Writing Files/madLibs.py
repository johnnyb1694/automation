# ---- Mad Libs program ----

# ---- Description ----

# This program allows the user to enter a combination of VERB, NOUN and ADJECTIVE placeholders in a given sample .txt file
# (see madLibsSample.txt as a reference example)

# ---- Specification ----

# This program needs to:
# 1. Read in the .txt file with the placeholders
# 2. Read in .txt file and establish how many placeholders there are for each category (e.g. how many NOUN, ADJECTIVE etc. placeholders there are)
# 3. According to the counts established in step 2, the program should request the user to provide appropriate inputs
# 4. Once the inputs have been provided, the placeholders need to be replaced
# 5. Finally, once the placeholders have been replaced, the resultant paragraph needs to be saved off to a new .txt file

# ---- Implementation ----

# Libraries
import re

# Stage 1: read in the relevant .txt file which contains the relevant placeholders
input_txt = open('madLibsSample.txt')

# Stage 2: read the contents of the sample .txt file to establish the count of each linguistic category
contents = input_txt.read()

# Stage 3: create a regex which can be used to identify nouns, adjectives and verbs
regex = re.compile(r'(ADJECTIVE|NOUN|VERB)')

matches = regex.findall(contents)

for m in matches:
    replacement = input(f'Please enter a {m}: ')
    contents = contents.replace(m, replacement, 1)

print(contents)
