# requires python3

import collections

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
days_in_month_dict = collections.OrderedDict([
    ('Jan', lambda leap_bool: 31),
    ('Feb', lambda leap_bool: 28 if not leap_bool else 29),
    ('Mar', lambda leap_bool: 31),
    ('Apr', lambda leap_bool: 30),
    ('May', lambda leap_bool: 31),
    ('Jun', lambda leap_bool: 30),
    ('Jul', lambda leap_bool: 31),
    ('Aug', lambda leap_bool: 31),
    ('Sep', lambda leap_bool: 30),
    ('Oct', lambda leap_bool: 31),
    ('Nov', lambda leap_bool: 30),
    ('Dec', lambda leap_bool: 31)])

# 0-6
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# 7th day is index 6
day_number = 0
leap_year = False
year_start = 1900
num_years = 101
number_sundays = 0

for year in range(year_start, year_start+num_years):
    if year % 4 == 0:
        if str(year)[-2] == '00' and year % 400 == 0:
            leap_year = False
        leap_year = True
    for month, days_in_month_func in days_in_month_dict.items():
        days_in_month = days_in_month_func(leap_year)
        day_name = days[day_number%7]
        extra = ''
        if year > year_start and day_name == 'Sun':
            number_sundays += 1
            extra = ' %s' % number_sundays
        print('%s 1st %s is a %s%s' % (month, year, day_name, extra))
        day_number += days_in_month

print('number_sundays=%s' % number_sundays)
