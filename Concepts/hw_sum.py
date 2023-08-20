import sys
sys.stdin = open('hw_input.txt', 'r')

T = 10

for _ in range(T):
    tc = int(input())
    N = 100
    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    
    max_num = 0
    # 최댓값 찾기: 가로
    for row in arr:
        row_sum = 0
        for num in row:
            row_sum += num
        
        if row_sum > max_num:
            max_num = row_sum
    
    # 최댓값 찾기: 세로
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += arr[i][j]
        
        if col_sum > max_num:
            max_num = col_sum
    
    # 최댓값 찾기: 대각선 왼쪽에서 오른쪽
    i = j = 0
    diag_sum = 0
    for _ in range(100):
        diag_sum += arr[i][j]
        i = j = i+1

    if diag_sum > max_num:
        max_num = diag_sum

    # 최댓값 찾기: 대각선 오른쪽에서 왼쪽
    i = 0
    j = N-1
    diag_sum = 0
    for _ in range(100):
        diag_sum += arr[i][j]
        i += 1
        j -= 1

    if diag_sum > max_num:
        max_num = diag_sum

    print("#%d %d" % (tc, max_num))