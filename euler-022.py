#!/usr/bin/env python3
filename = 'p022_names.txt'

with open(filename, 'r') as tfile:
    all_names = tfile.read().replace("\"", '')
all_names = all_names.split(',')
all_names.sort()

total_score = 0
print('name, index, name_score, total_score')
for ind, name in enumerate(all_names):
    index = ind + 1
    name_score = 0
    for char in name:
        # ord('A') = 65 so if we - 64 we get 1
        name_score += ord(char) - 64
    name_score *= index
    total_score += name_score
    print('%s %s %s %s' % (name, index, name_score, total_score))
print('total_score=%s' % total_score)
