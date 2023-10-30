# V = Vertex의 갯수
# AM = Matrix
# sv = starting vertex

edges = [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (4, 6), (5, 6)]
V, E = 7, 8

# Matrix
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1

def DFS(V, AM, sv):
    visited = [0] * (V+1)
    # 스택에 시작 정점을 푸쉬
    stack = [sv]
    # 디버깅용: 방문한 리스트 순서를 기록할 리스트
    travel = []
    # 스택에 내용이 있는 동안 반복
    while len(stack):
        # 스택에서 pop
        node = stack.pop()
        travel.append(node)
        # 방문 했는지 안했는지 확인
        # 방문 했으면 방문 표시
        if not visited[node]:
            visited[node] = 1
        # 인접한 노드 중에서 방문하지 않은 노드 체크
        for i in range(1, V+1):
            if AM[node][i] == 1 and visited[i] == 0:
                stack.append(i)
    print(stack)
    print(visited)
    print(travel)

print(DFS(V, AM, 1))

        
