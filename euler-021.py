#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10,000
"""


def divisors(big_num):
    divisors = []
    upper_bound = big_num/2
    for divisor in range(1, upper_bound+1):
        if big_num % divisor == 0:
            divisors.append(divisor)
    return divisors

def calc_divisor_sum(big_num):
    return sum(divisors(big_num))

divisor_sums = {}
amicable_numbers_sum = 0
for num in range(2,10000):
    divisor_sum = calc_divisor_sum(num)
    divisor_sums[num] = divisor_sum
    if (divisor_sum in divisor_sums
            and divisor_sums[divisor_sum] == num
            and num != divisor_sum):
        print('amicable pair %s %s' % (num, divisor_sum))
        amicable_numbers_sum += divisor_sum + num

print('=amicable_numbers_sum%s' % amicable_numbers_sum)
