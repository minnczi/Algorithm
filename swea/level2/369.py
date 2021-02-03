T = int(input())
import time

for test_case in range(1, T + 1):
    target = int(input())
    # three six nine
    tsn = ['3', '6', '9']

    result_list = []
    for i in range(1, target+1):
        is_tsn = 0
        for digit in str(i):
            if digit in tsn:
                is_tsn += 1
        if is_tsn:
            result_list.append('-' * is_tsn)
        else:
            result_list.append(str(i))


