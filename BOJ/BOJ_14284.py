# BOJ14284
# 다익스트라 알고리즘 사용
from heapq import heappush
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
# 연결관계를 표시할 AL
AL = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    heappush(AL[a], [c, b])
    heappush(AL[b], [c, a])


s, t = map(int, input().split())
visited = [1] + [0]*N
# s-->e까지 도달하는데 필요한 최소 가중치
min_weights = [1000000] * (N+1) 
min_weights[s] = 0
idx = s

while 0 in visited:
    visited[idx] = 1
    weight = min_weights[idx]
    # 비용 업데이트 하기
    for node in AL[idx]:
        # 현재 노드의 weight + 다음 노드로 가는 비용 < 현재 저장되어있는 다음 노드의 비용 이라면
        if weight+node[0] < min_weights[node[1]]:
            min_weights[node[1]] = weight+node[0]

    # 방문하지 않은 노드 중에 가장 비용이 적게 드는 노드 고르기
    min_weight = 1000000
    for i in range(1, N+1):
        if not visited[i] and min_weights[i] < min_weight:
            min_weight = min_weights[i]
            idx = i
    
print(min_weights[t])