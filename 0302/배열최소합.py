import sys
sys.stdin = open('min_sum_input.txt', 'r')

T = int(input())

# 특정행에서 사용할 열을 선택함
def find_min_sum(total, row):
    global minimum
    if total >= minimum:
        return

    if row >= N:
        if total < minimum:
            minimum = total
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            find_min_sum(total+arr[row][col], row+1)
            visited[col] = 0
    


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    minimum = 500
    total = 0
    r = 0
    visited = [0] * N
    find_min_sum(total, r)
    print(minimum)