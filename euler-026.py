import decimal as de
import math


def has_cycles(substring, remaining_str):
    num_cycles = 0
    while True:
        index = remaining_str.find(substring)
        if index != 0:
            return False
        num_cycles += 1
        remaining_str = remaining_str[len(substring):]
        if len(remaining_str) < len(substring):
            if substring.find(remaining_str) == 0:
                return True
    return True


def max_reoccurring_cycle(str_num):
    # for each digit and looking back
    max_index = math.ceil(len(str_num)/2)
    for first_index in range(max_index):
        for second_index in range(first_index+1,max_index):
            substring = str_num[first_index:second_index]
            remaining_str = str_num[second_index:]
            if has_cycles(substring, remaining_str):
                return len(substring)
    return None

max_cycle_length = -1
max_cycle_number = None
# key = number, val is cycle length
cycles = {}

for num in range(1,1001):
    print('num=%s' % num)
    # per wikipedia the period for 1/k is always <= k-1
    # so we make the max string size 2*k
    de.getcontext().prec = num*2
    fraction_val = str(de.Decimal(1) / de.Decimal(num))
    if len(fraction_val) > 5:
        cycle_length = max_reoccurring_cycle(fraction_val)
        if cycle_length:
            cycles[num] = cycle_length
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_cycle_number = num
print('cycles=%s' % cycles)
print('max_cycle_length=%s' % max_cycle_length)
print('max_cycle_number=%s' % max_cycle_number)
