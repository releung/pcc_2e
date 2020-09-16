#!/usr/bin/env python
# coding=UTF-8

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name.
"""

name = ['elliot', 'ada', 'bier']
format_pattern = 'Hello, {}.'
print(format_pattern.format(name[0].title()))
print(format_pattern.format(name[1].title()))
print(format_pattern.format(name[2].title()))

# 或者迭代
for n in name:
    print(format_pattern.format(n.title()))

