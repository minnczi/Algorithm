import sys
sys.stdin = open('miro_input.txt', 'r')

T = int(input())

# 델타 (상하좌우 순으로)
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(sr, sc):
    dist = [[0] * (N+2) for _ in range(N+2)]
    queue = [[sr, sc]]
    dist[sr][sc] = 1
    while queue:
        cr, cc = queue.pop(0)
        new_dist = dist[cr][cc] + 1
        for dr, dc in drc:
            if maze[cr+dr][cc+dc] == 3:
                return new_dist-2
            # maze에서 0이고 아직 방문하지 않았다면
            if not maze[cr+dr][cc+dc] and not dist[cr+dr][cc+dc]:
                dist[cr+dr][cc+dc] = new_dist
                queue.append([cr+dr, cc+dc])
    return 0

for tc in range(1, T+1):
    N = int(input())

    # maze input 받기 + 시작점(2) 찾기
    maze = [[1] * (N+2)]
    for i in range(1, N+1):
        temp = [1] + list(map(int, input())) + [1]
        for j in range(N+2):
            if temp[j] == 2:
                sr, sc = i, j
        maze.append(temp)
    maze += [[1] * (N+2)]
    result = bfs(sr, sc)
    print("#%d %d" % (tc, result))