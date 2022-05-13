N, M = map(int, input().split())
AL = [list() for _ in range(N+1)]

# 연결 간선들을 표시하는 adjacent list
for _ in range(M):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)

dist_cnt = 0 # 같은 거리를 가진 헛간의 갯수
prev_dist = 0 # 바로 직전 헛간 까지의 최소 거리
hide = 0 # 숨을 헛간
visited = [1,1] + [0] * (N-1)
queue = [[1,0]]

while queue:
    node, dist = queue.pop(0)
    # 연결된 헛간 중에 아직 방문하지 않은 헛간이 있다면 추가
    for i in AL[node]:
        if not visited[i]:
            visited[i] = 1
            queue.append([i, dist+1])

    # 1. 바로 직전 방문한 헛간보다 멀리 떨어져 있다면 헛간 위치와 거리 갱신
    if dist != prev_dist:
        prev_dist = dist
        dist_cnt = 0
        hide = node
    # 2. 바로 직전 방문한 헛간과 같은 거리에 있다면 둘중 번호가 작은 것 찾기
    else:
        hide = min(hide, node)
    # 같은 거리에 있는 헛간 갯수 1개 추가
    dist_cnt += 1

print(hide, prev_dist, dist_cnt)