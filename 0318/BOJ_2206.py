# BOJ 2206 벽 부수고 이동하기
# BFS로 접근
import sys
sys.stdin = open('2206_input.txt', 'r')


# 이동 가능 방향
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs():
    # 시작 지점: cr, cc, 벽 부술 수 있는 남은 횟수를 배열로 저장
    queue = [[0, 0, 1]]
    # 현재 지점에서의 거리 저장 (1, 1에서의 거리는 1)
    dist[0][0] = 1
    while queue:
        cr, cc, matchang = queue.pop(0)
        for dr, dc in drc:
            nr, nc = cr+dr, cc+dc
            print(cr, cc, nr, nc, matchang)
            # 도착 지점에 도착한 경우
            if (nr == N-1) and (nc == M-1):
                return dist[cr][cc] + 1
            # 아직 방문하지 않은 길이 있으면 한칸 더 가서
            if not dist[nr][nc] and (0 <= nr < N) and (0 <= nc < M):
                dist[nr][nc] = dist[cr][cc] + 1
                # 열려있는 길을 만났을때
                if arr[nr][nc] == 0:
                    queue.append([nr, nc, matchang])
                # 닫혀 있는 길이지만, 아직 길을 부술수 있는 기회가 한번 남았을때
                elif arr[nr][nc] and matchang:
                    queue.append([nr, nc, 0])
    return -1

# input 받아오기
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

# 방문 체크용 배열 --> 각 칸마다 현재 칸에 도착할 수 있는 최소 거리를 저장, 현재 칸은 1
dist = [[0]*(M+2) for _ in range(N+2)]

print(bfs())

