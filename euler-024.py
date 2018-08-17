# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def get_permutations(input_list):
    if len(input_list) <= 1:
        return [input_list]
    else:
        results = []
        for ind, val in enumerate(input_list):
            remaining_list = input_list[:ind] + input_list[ind+1:]
            permutations = get_permutations(remaining_list)
            for permutation in permutations:
                permutation.insert(0, val)
                results.append(permutation)
        return results

permutations = get_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# first is index 0
# millionth is index? 1,000,000 --> 999,999
print('length_of_permutations=%s' % len(permutations))
print('millionth_permutation=%s' % permutations[999999])
