import sys
from itertools import combinations

sys.stdin = open('17471_input.txt', 'r')

"""
BOJ 17471: 게리멘더링
1. 한 선거구 안에 들어갈 수 있는 모든 부분집합을 구한다
1-1. 전체 인구가 N이라면 1, 2... N//2명인까지의 부분집합(한 선거구의 인구)을 보면 모든 경우의 수를 구할 수 있다
1-2. 인구의 수가 비슷하면 합이 비슷할 가능성이 높으므로, N//2명인 부분집합부터 역순으로 탐색
2. 두 선거구의 인구의 차이를 구한 뒤 현재 min 보다 작으면 진행
3. 각 선거구에 있는 구역들만 포함해서 각자 DFS를 돌려서 모든 노드가 연결되어 있는지 체크
4. 2번 3번이 모두 충족되었을때만 min값을 업데이트
"""

N = int(input())
P = [0] + list(map(int, input().split()))
AL = [[]] + [list(map(int, input().split())) for _ in range(N)]


def DFS(zone, zone_link):
    visited = [0] * (N+1)
    
    # DFS 시작점 찾아서 스택에 넣기
    stack = [zone[0]]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = 1
            for i in zone_link[current]:
                stack.append(i)
    
    # 모든 지점이 연결됐는지 체크
    for i in zone:
        if visited[i] == 0:
            return 0
    return 1

min_diff = 100000
for i in range(1, N//2+1):
    # 한 선거구에 i명이 들어가는 모든 부분 집합
    zones = list(combinations(range(1, N+1), i))
    for zone1 in zones:
        # 각 선거구에 몇명이 있는지 구하기
        p1, p2 = 0, 0
        zone2 = []
        zone1_link, zone2_link = [[] for _ in range(N+1)], [[] for _ in range(N+1)]
        for i in range(1, N+1):
            if i in zone1:
                p1 += P[i]
                zone1_link[i] = AL[i]
            else:
                p2 += P[i]
                zone2.append(i)
                zone2_link[i] = AL[i]


        # 두번째 분기: 두 선거구가 다 연결되어 있다면 min_diff 값 치환
        result1 = DFS(zone1, zone1_link)
        result2 = DFS(zone2, zone2_link)

        if result1 and result2:
            # 첫번째 분기: 만약 p1, p2의 인원차이가 현재 min보다 크다면, 더이상 체크 할 필요 없음
            if abs(p1-p2) < min_diff:
                min_diff = abs(p1-p2)
        
if min_diff == 100000:
    min_diff = -1

print(min_diff)