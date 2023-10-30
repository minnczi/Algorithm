edges = [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (4, 6), (5, 6)]
V, E = 7, 8

# List
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
print(AL)

# v는 방문되지 않은 정점으로, 방문하러 들어옴
# visited[v] = 1 -> 방문처리를 한다
# 물리적인 스택이 필요가 없음 (시스템 스택에 의해서 순서대로 처리가 된다)
travel = []
visited = [0] * (V+1)
def DFS_re(AL, node, visited):
    visited[node] = 1
    travel.append(node)
    for i in AL[node]:
        if not visited[i]:
            DFS_re(AL, i, visited)

DFS_re(AL, 1, visited)