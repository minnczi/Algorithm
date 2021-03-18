import sys
sys.stdin = open('2819_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = set()

def find_num(cr, cc, num):
    if len(num) == 7:
        result.add(num)
        return
    
    for i in range(4):
        row, col = cr+dr[i], cc+dc[i]
        if arr[row][col] != -1:
            find_num(row, col, num + arr[row][col])

T = int(input())
for tc in range(1, T+1):
    N = 4
    # input 받아서 벽 만들기
    arr = [[-1]*(N+2)]
    for _ in range(N):
        arr.append([-1] + list(input().split()) + [-1])
    arr.append([-1]*(N+2))

    for i in range(1, N+1):
        for j in range(1, N+1):
            find_num(i, j, arr[i][j])
    
    print("#{} {}".format(tc, len(result)))
