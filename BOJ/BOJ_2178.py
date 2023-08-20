import sys
sys.stdin = open('2178_input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(arr):
    queue = []
    visited = [[0]*(M+2) for _ in range(N+2)]
    # [행의좌표, 열의좌표, 현재까지 최소거리]를 배열로 묶어 queue에 저장
    queue.append([1, 1, 1])
    visited[1][1] = 1

    while True:
        cr, cc, dist = queue.pop(0)
        if (cr == N) and (cc == M):
            return dist

        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            if arr[nr][nc] == 1 and not visited[nr][nc]:
                queue.append([nr, nc, dist+1])
                visited[nr][nc] = 1


# N = 행의 갯수, M = 열의 갯수
N, M = map(int, input().split())
# 벽과 함께 미로 받아오기
arr = [[0] + list(map(int, input())) + [0] for _ in range(N)]
arr.insert(0, [0] * (M+2))
arr.append([0] * (M+2))
print(bfs(arr))
