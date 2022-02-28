"""
BOJ 18352: 특정 거리의 도시 찾기
"""
from collections import deque

N, M, K, X = map(int, input().split())

# cities[x] -> x와 연결되어 있는 모든 도시들을 나열한 리스트
# 예시) cities[1] = [2, 3] -> 1과 직접적으로 연결되어 있는 도시는 2, 3
cities = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    cities[a].append(b)

# 최단 거리를 찾기 위한 BFS
def find_k_dist_cities():
    queue = deque([[X,0]])
    visited = [0] * (N+1)
    visited[X] = 1
    ans = set()

    while queue:
        current, dist = queue.popleft()
        if dist > K:
            break

        elif dist == K:
            ans.add(current)
            continue
        
        for city in cities[current]:
            if not visited[city]:
                visited[city] = 1
                queue.append([city, dist+1])
    return ans

ans = find_k_dist_cities()

if not ans:
    print(-1)
else:
    ans = sorted(list(ans))
    for i in ans:
        print(i)