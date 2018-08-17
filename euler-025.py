# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?
import math

def find_fib(num_digits_required):
    """Calculates the first fib number with num_digits_required"""
    last_fib = 0
    current_fib = 1
    index = 1
    current_num_digits = len(str(current_fib))
    while current_num_digits < num_digits_required:
        print('fib=%s index=%s current_num_digits=%s' %
              (current_fib, index, current_num_digits))
        next_fib = last_fib + current_fib
        last_fib = current_fib
        current_fib = next_fib
        index += 1
        current_num_digits = len(str(current_fib))
    print('fib=%s index=%s current_num_digits=%s' %
          (current_fib, index, current_num_digits))
    return current_fib

find_fib(1000)
