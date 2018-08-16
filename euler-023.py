#!/usr/bin/env python3

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
import math

def is_abundant_number(num):
    divisor_sum = 0
    upper_bound = math.ceil(num/2)
    for divisor in range(1, upper_bound+1):
        if num % divisor == 0:
            divisor_sum += divisor
    if divisor_sum > num:
        return True
    return False

# find the set of all abundent numbers
abundant_numbers = set()
for num in range(1,28123+1):
    if is_abundant_number(num):
        abundant_numbers.add(num)
print('done finding abundant numbers, total_num=%s' % len(abundant_numbers))

# then go through all numbers and subtract every abundant number and find if
# the remainder is abundant, if not, then we have non abundantsum number
num_abundantsum_numbers = []
for num in range(1,28123+1):
    abundantsum_number = False
    for abundant_number in abundant_numbers:
        if abundant_number >= num:
            continue
        remainder = num - abundant_number
        if remainder in abundant_numbers:
            abundantsum_number = True
            break
    if not abundantsum_number:
        num_abundantsum_numbers.append(num)
print('num_abundantsum_numbers=%s' % len(num_abundantsum_numbers))
non_absum = sum(num_abundantsum_numbers)
print('non_absum=%s' % non_absum)
