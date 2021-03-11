import sys
from itertools import combinations
from copy import deepcopy

sys.stdin = open('14502_input.txt', 'r')

max_safe = 0

# dxy 상하좌우 순서
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def get_safezones(room, walls):
    # 벽 세우기 
    for wall in walls:
        room[wall[0]][wall[1]] = 1
    
    # 바이러스가 있는 위치 찾기
    queue = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            if room[i][j] == 2:
                queue.append([i, j])
    
    # 바이러스 퍼트리기
    while queue:
        current = queue.pop(0)
        for i in range(4):
            row = current[0]+dxy[i][0]
            col = current[1]+dxy[i][1]
            if room[row][col] == 0:
                room[row][col] = 2
                queue.append([row, col])

    # 안전지대 갯수세기
    safe = 0
    for row in room:
        for col in row:
            if col == 0:
                safe += 1

    # 현재 min과 비교하기
    global max_safe
    if safe > max_safe:
        max_safe = safe
    return


N, M = map(int, input().split())
empty = []
arr =  [[1] + list(map(int, input().split())) + [1] for _ in range(N)]
arr.insert(0, [1] * (M+2))
arr.append([1] * (M+2))

# 벽을 세울 수 있는 곳을 마킹
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 0:
            empty.append((i, j))

# 벽을 세개 세울수 있는 모든 콤비네이션
cases = list(combinations(empty, 3))
for walls in cases:
    room = deepcopy(arr)
    get_safezones(room, walls)

print(max_safe)
