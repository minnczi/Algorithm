import sys
from copy import deepcopy
sys.stdin = open('2206_input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(arr):
    # visit 배열을 두개 만든다: 하나는 벽을 안깬상태에서 방문하는것, 하나는 벽을 깬 상태에서 방문하는것
    # 이렇게 만드는 이유는 똑같은 칸에 있더라도 벽을 깰 찬스를 썼는지 안썼는지에 따라 최단거리가 달라지기때문
    visited = [[[0, 0] for _ in range(M+2)] for _ in range(N+2)]

    # queue에 배열을 저장한다
    # [행의 좌표, 열의 좌표, 현재까지의 최단거리, 벽을 부쉈는지 여부(0=안부심, 1=부심)]
    queue = [[1, 1, 1, 0]]
    
    while queue:
        cr, cc, dist, wall = queue.pop(0)
        visited[cr][cc][wall] = 1
        # 도착지점에 도착했다면 dist를 반환
        if cr == N and cc == M:
            return dist
        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            # wall = 0 일때
            if not visited[nr][nc][wall]:
                # 그냥 지나가기
                if arr[nr][nc] == 0:
                    queue.append([nr, nc, dist+1, wall])
                    visited[nr][nc][wall] = 1
                # 벽 부수고 지나가기
                elif (arr[nr][nc] == 1) and (wall == 0) and (visited[nr][nc][wall] == 0):
                    queue.append([nr, nc, dist+1, 1])
                    visited[nr][nc][wall] = 1
                    visited[nr][nc][1] = 1
                
    return -1


# N = 행의 갯수, M = 열의 갯수
N, M = map(int, input().split())
# 벽과 함께 미로 받아오기
arr = [[1] + list(map(int, input())) + [1] for _ in range(N)]
arr.insert(0, [1] * (M+2))
arr.append([1] * (M+2))
print(bfs(arr))