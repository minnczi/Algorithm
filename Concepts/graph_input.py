edges = [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (4, 6), (5, 6)]
V, E = 7, 8

# Matrix (AM)
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
print(AM)

# List (AL)
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
print(AL)

# Two Way Matrix
AM = [[0]*(V+1) for _ in range(V+1)]
for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1
print(AM)

# Two Way List
AL = [[] for _ in range(V+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s)
print(AL)
