V, E = 5, 6
edges = [(1, 2), (2, 3), (1, 4), (2, 4), (1, 5), (3, 5)]

# make Adjacent Matrix
AM = [[0]*(V+1) for _ in range(V+1)]

for s, e in edges:
    AM[s][e] = 1

for line in AM:
    print(line)

# make Adjacent List
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)

for v in range(1, V+1):
    if AL[v]:
        print(v, AL[v])

# 양방향 Adjacent Matrix 만들기
AM = [[0]*(V+1) for _ in range(V+1)]

for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1

for line in AM:
    print(line)

# 양방향 Adjacent List 만들기
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s)

for v in range(1, V+1):
    if AL[v]:
        print(v, AL[v])