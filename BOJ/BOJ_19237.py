import pprint
from heapq import heappush, heappop
"""
방향: 1(위), 2(아래), 3(왼쪽), 4(오른쪽)
"""
N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dir = list(map(int, input().split()))
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

queue = []
for i in range(N):
    for j in range(N):
        shark = board[i][j]
        if shark:
            board[i][j] = [shark, shark, K] # [칸에 있는 상어, 냄새 뿌린 상어, 초]
            heappush(queue, [shark, i, j])

time = 0
while queue:
    time += 1
    shark, i, j = heappop(queue)