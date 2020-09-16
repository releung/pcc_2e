#!/usr/bin/env python
# coding=UTF-8

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print() call at the end
        of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
        the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
        in your list.
"""

guest_list = ['lao zu', 'confucius', 'sun tzu', 'mao zedong', 'deng xiaoping']

invite_pattern = "Hello {}, please come to dinner."
for name in guest_list:
    print(invite_pattern.format(name.title()))

can_not_come_people = guest_list.pop(0)
print("\nSorry, {} can't make it dinner.\n".format(can_not_come_people.title()))

new_guest = 'Michael Jackson'
guest_list.insert(0, new_guest)
for name in guest_list:
    print(invite_pattern.format(name.title()))


