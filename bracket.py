'''
This is just a quick little bracket maker and randomizer for work ping pong
tournaments. It should, given a list of registrants, pair them into an
appropriately sized bracket and print out the list of pairs.

May make this print to an excel document, or simply to a document.

(c) Keith Diedrick, 2017
'''

import sys
import os
import random

if len(sys.argv) < 2:
    raise ValueError("Please provide the name of the file containing names to be paired. Please make sure the names are comma separated.")
else:
    inNames = sys.argv[1]

with open(inNames) as i:
    names = i.read().split(',')

s_names = []

for entry in names:
    s_names.append(entry.strip())


if len(s_names)%2 != 0:
    s_names.append('bye')

random.shuffle(s_names)

for i in range(0, len(s_names)-1, 2):
    print(s_names[i])
    print(' vs. ')
    print(s_names[i+1])
    print('\n')
