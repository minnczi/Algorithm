"""
N = 실험관의 크기
K = 바이러스 종류의 갯수
S = 시간
X, Y = X, Y 좌표
"""
from collections import deque

N, K = map(int, input().split())
lab = [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
lab.insert(0, [-1] * (N+2))
lab.append([-1] * (N+2))

S, X, Y = map(int, input().split())

# 상하좌우 순서로 주변 탐색
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

queue = deque()
for k in range(1, K+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if lab[i][j] == k:
                queue.append([i, j, 0])

while queue:
    r, c, t = queue.popleft() # row, col, time

    if t == S:
        break

    for dr, dc in drc:
        if not lab[r+dr][c+dc]:
            lab[r+dr][c+dc] = lab[r][c]
            queue.append([r+dr, c+dc, t+1])

print(lab[X][Y])
