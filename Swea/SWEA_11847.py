# SWEA 11847 최소합
import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 1]
dc = [1, 0]

def dfs(arr):
    visited = [[0]*(N+1) for _ in range(N+1)]
    queue = [[1, 1]]
    while queue:
        r, c = queue.pop(0)
        # arr[r][c]칸 까지 가는 최소 거리 구하기
        up, left = arr[r-1][c], arr[r][c-1]
        if up and left:
            arr[r][c] += min(up, left)
        elif up:
            arr[r][c] += up
        elif left:
            arr[r][c] += left

        # 다음에 갈 칸 정하기
        for i in range(2):
            nr, nc = r+dr[i], c+dc[i]
            if nr <= N and nc <= N and not visited[nr][nc]:
                queue.append([nr, nc])
                visited[nr][nc] = 1
    return arr[N][N]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+1)]
    for _ in range(N):
        arr.append([0] + list(map(int, input().split())))
    print("#%d %d" % (tc, dfs(arr)))