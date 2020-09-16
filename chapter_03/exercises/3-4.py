#!/usr/bin/env python
# coding=UTF-8

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

guest_list = ['lao zu', 'confucius', 'sun tzu', 'mao zedong', 'deng xiaoping']

invite_pattern = "Hello {}, please come to dinner."

for name in guest_list:
    print(invite_pattern.format(name.title()))

