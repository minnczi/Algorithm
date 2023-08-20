import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T+1):
    num = int(input())
    factor_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    factors = factor_dict.keys()

    while num >= 2:
        for i in factors:
            if num % i == 0:
                num = num / i
                factor_dict[i] += 1
                break

    print('#%d %d %d %d %d %d' % (t, factor_dict[2], factor_dict[3], factor_dict[5], factor_dict[7], factor_dict[11]))
