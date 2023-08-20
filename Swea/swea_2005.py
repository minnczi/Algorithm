T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[1]]

    # 2번째(idx=1)부터 N(idx=N-1)번째 줄까지
    for i in range(1, N):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)
        pascal.append(row)
    
    print("#%d" % (tc))
    # print('\n'.join(' '.join(map(str, row)) for row in pascal))
    for row in pascal:
        print(" ".join(list(map(str, row))))
    

# for tc in range(1, T+1):
#     N = int(input())
#     print("#%d\n%s" % (tc, '1'))
    
#     current = '1 1'
#     for i in range(2, N+1):
#         prev_arr = list(map(int, current.split()))
#         print(current)
#         current = '1'
#         for j in range(1, i):
#             current += ' ' + str(prev_arr[j-1]+prev_arr[j])
#         current += ' 1'

