def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

roads = []
for _ in range(M):
    x, y, z = map(int, input().split())
    roads.append((z, y, x))

roads.sort()

parent = [i for i in range(N)]
ans = 0
for road in roads:
    z, x, y = road
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
    else:
        ans += z

print(ans)