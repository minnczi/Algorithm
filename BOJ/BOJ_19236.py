from copy import deepcopy
from heapq import heappush, heappop

# 12시 방향을 기준으로 반시계 방향으로 한칸씩 이동할때 움직이는 값
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# 4x4 크기의 탱크
tank = [list() for _ in range(4)]
# 물고기의 좌표를 저장할 별도의 배열
fish = [[0,0] for _ in range(17)]


# 입력 받기
# [물고기번호, 방향] 형태로 2차원 리스트에 저장
# 상어 = 0, 빈칸 = -1
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        tank[i].append([temp[j], temp[j+1]-1])
        fish[temp[j]] = [i, j//2]

max_total = 0 
total = 0

def dfs(tank, fish, total, sr, sc):  
    global max_total

    # 상어 -> 물고기 먹기
    num, dir = tank[sr][sc] # 잡아 먹히는 물고기 번호와 방향
    total += num
    tank[sr][sc] = [0, dir] # 상어 이동
    fish[num] = [-1, -1] # 물고기 쥬금...
    max_total = max(max_total, total)

    # 물고기 이동
    for num in range(1, 17):
        fr, fc = fish[num] # 물고기 좌표
        dir = tank[fr][fc][1] # 방향

        if fr == -1 or 0:
            continue

        for i in range(8):
            nfr, nfc = fr + dr[dir], fc + dc[dir]
            # 움직이는 위치가 범위내에 있고, 해당 칸이 상어가 아닐 경우
            if 0 <= nfr < 4 and 0 <= nfc < 4 and tank[nfr][nfc][0] != 0:
                temp = tank[nfr][nfc] # 자리가 바뀔 물고기
                tank[nfr][nfc] = [num, dir]
                tank[fr][fc] = temp
                fish[num] = [nfr, nfc]
                if temp[0] > 0:
                    fish[temp[0]] = [fr, fc]
                break
            else:
                dir = (dir+1) % 8

    # 상어 이동
    dir = tank[sr][sc][1] # 방향
    # 최소 1칸, 최대 3칸 이동 가능
    for i in range(1, 4):
        nsr, nsc = sr+dr[dir]*i, sc+dc[dir]*i
        if 0 <= nsr < 4 and 0 <= nsc < 4 and tank[nsr][nsc][0] > 0:
            tank[sr][sc] = [-1, -1]
            dfs(deepcopy(tank), deepcopy(fish), total, nsr, nsc)
            tank[sr][sc] = [0, dir]

dfs(tank, fish, 0, 0, 0)
print(max_total)