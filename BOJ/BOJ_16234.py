N, L, R = map(int, input().split())

map = [[1000] + list(map(int, input().split())) + [1000] for _ in range(N)]
map.insert(0, [1000] * (N+2))
map.append([1000] * (N+2))

# 하 우 상 좌 순서
drc = [[1,0], [0,1], [-1,0], [0,-1]]


def dfs(allies):
    visited = [[1] + [0]*N + [1] for _ in range(N)]
    visited.insert(0, [1]*(N+2))
    visited.append([1]*(N+2))

    for r in range(1,N+1):
        for c in range(1,N+1):
            if not visited[r][c]:
                visited[r][c] = 1
                stack = [[r,c]]
                countries = [[r,c]] # r,c와 연결되어 있는 나라의 리스트
                pop = map[r][c] # 연결된 나라들의 총 인구 수
                while stack:
                    cr, cc = stack.pop()
                    for ar, ac in allies[cr][cc]:
                        if not visited[ar][ac]:
                            visited[ar][ac] = 1
                            stack.append([ar,ac])
                            countries.append([ar,ac])
                            pop += map[ar][ac]
                
                avg_pop = pop // len(countries)
                for cr, cc in countries:
                    map[cr][cc] = avg_pop


# 1단계: 국경이 열린 곳을 표기하기
days = 0

while True:
    move = False
    allies = [[[] for _ in range(N+2)] for _ in range(N+2)]
    for r in range(1,N+1):
        for c in range(1,N+1):
            for dr, dc in drc[:2]:
                # 인접한 곳들 중 인구차가 L과 R사이에 있는 나라가 있다면, allies 배열에 추가
                if L <= abs(map[r][c] - map[r+dr][c+dc]) <= R:
                    allies[r][c].append([r+dr, c+dc])
                    allies[r+dr][c+dc].append([r, c])
                    move = True
    # 국경이 단한곳도 열리지 않았다면 -> 인구이동 X
    if not move:
        break
    # 국경이 한곳이라도 열렸다면 -> 인구이동 O
    else:
        days += 1
        dfs(allies)

print(days)
