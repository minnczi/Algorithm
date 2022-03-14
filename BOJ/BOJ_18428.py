from itertools import combinations
from copy import deepcopy

N = int(input())
hallway = [["O"] + list(input().split()) + ["O"] for _ in range(N)]
hallway.insert(0, [1]*(N+2))
hallway.append([1]*(N+2))
teachers = []
blank = []
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]


for r in range(N):
    for c in range(N):
        if hallway[r][c] == "T":
            teachers.append([r,c])
        elif hallway[r][c] == "X":
            blank.append([r,c])

def dfs(combi):
    visited = deepcopy(hallway)
    stack = deepcopy(teachers)
    for r, c in combi:
        visited[r][c] = "O"
    
    while stack:
        r, c = stack.pop()
        for dr, dc in drc:
            if visited[r+dr][c+dc] == "S":
                return "NO"
            elif visited[r+dr][c+dc] == "X":
                stack.append([r+dr, c+dc])
                visited[r+dr][c+dc] = "O"
    return "YES"
            
    
obs_combi = combinations(blank, 3)

for combi in obs_combi:
    if dfs(combi) == "YES":
        print("YES")
        break
else:
    print("NO")
