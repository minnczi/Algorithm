# delta 사용
import sys
sys.stdin = open('ex01input.txt', 'r')

T = int(input())

for tc in range(1, T+1): 
    Arr = []
    # input 받기
    for _ in range(5):
        lst = list(map(int, input().split()))
        Arr.append(lst)
    
    # 상하좌우 순으로 인접한 곳과의 인덱스 차이
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # # 방법 1: dr, dc를 따로 저장하고 사용
    # total = 0
    # for i in range(5):
    #     for j in range(5):
    #         diff = 0
    #         for k in range(4):
    #             # 인접한 곳의 인덱스 구하기
    #             nr = i + dr[k]
    #             nc = j + dc[k]

    #             # 만약 실제 존재하는 인덱스라면 더해주기
    #             if 0 <= nr < 5 and 0 <= nc < 5:
    #                 total += abs(Arr[nr][nc] - Arr[i][j])
    
    # 방법 2: dxy를 사용
    total = 0 
    for i in range(5):
        for j in range(5):
            diff = 0
            for dr, dc in dxy:
                # 인접한 곳의 인덱스 구하기
                nr = i + dr
                nc = j + dc

                # 만약 실제 존재하는 인덱스라면 더해주기
                if 0 <= nr < 5 and 0 <= nc < 5:
                    total += abs(Arr[nr][nc] - Arr[i][j])

    print("#%d %d" % (tc, total))