# requires python3

def calculate_nfactorial(n):
    res = 1
    for num in range(n,1, -1):
        res *= num
    return res

result_integer = calculate_nfactorial(100)
print('result_integer=%s' % result_integer)
sum = 0
for char in str(result_integer):
    sum += int(char)
print('sum=%s' % sum)
