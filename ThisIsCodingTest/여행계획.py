def find(parent, x):
    # 최상위 노드가 아닐경우
    if parent[x] != x:
        # 자기보다 더 위에 있는 노드를 찾아 이동
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    # 둘 중 더 작은 노드를 parent 노드로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# input 값 받기
N, M = map(int, input().split())
travel = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

# 자기 자신을 parent로 초기 설정
parent = [i for i in range(N)]

# 각 여행지별로 루트 노드를 찾는다
for i in range(N):
    for j in range(N):
        if travel[i][j]:
            union(parent, i, j)

# 여행 하는 모든 곳들의 루트 노드가 같은 부모인지를 확인한다
root = parent[0]
for p in plan:
    # 부모 노드가 루트 노드와 다르다 - 연결되어 있지 않음
    if parent[p-1] != root:
        print('NO')
        break
else:
    print('YES')
