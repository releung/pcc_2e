#!/usr/bin/env python
# coding=UTF-8

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""

cars = ['TOYOTA', 'Volkswagen', 'RollsRoyce', 'Porsche']

farmat_pattern = 'I would like to own a {} car.'
for car in cars:
    print(farmat_pattern.format(car.title()))





