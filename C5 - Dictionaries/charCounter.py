import pprint

message = input('Please type in a message and I will count every character: ')

counts = {}

for character in message:
    counts.setdefault(character, 0)
    counts[character] = counts[character] + 1

pprint.pprint(counts)
