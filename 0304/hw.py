import sys
sys.stdin = open('1226_input.txt', 'r')

drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(sr, sc):
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] == 1
    stack = [[sr, sc]]

    while stack:
        sr, sc = stack.pop()
        if miro[sr][sc] == 3:
            return 1
        visited[sr][sc] = 1
        for dr, dc in drc:
            if miro[sr+dr][sc+dc] != 1 and not visited[sr+dr][sc+dc]:
                stack.append([sr+dr, sc+dc])
    return 0


T = 10
for _ in range(T):
    tc = int(input())
    miro = []
    N = 16
    for r in range(N):
        arr = list(map(int, input()))
        for c in range(N):
            if arr[c] == 2:
                sr, sc = r, c
        miro.append(arr)
    result = dfs(sr, sc)
    print("#%d %d" % (tc, result))