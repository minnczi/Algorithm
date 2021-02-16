import sys
sys.stdin = open('ex01input.txt', 'r')

T = int(input())

for tc in range(1, T+1): 
    Arr = []
    # input 받기
    for _ in range(5):
        lst = list(map(int, input().split()))
        Arr.append(lst)
    
    total = 0
    for i in range(5):
        for j in range(5):
            diff_up = (0 if i==0 else abs(Arr[i][j] - Arr[i-1][j]))
            diff_down = (0 if i==4 else abs(Arr[i][j] - Arr[i+1][j]))
            diff_left = (0 if j==0 else abs(Arr[i][j] - Arr[i][j-1]))
            diff_right = (0 if j==4 else abs(Arr[i][j] - Arr[i][j+1]))
            diff_total = diff_up + diff_down + diff_left + diff_right
            total += diff_total
    print("#%d %d" % (tc, total))