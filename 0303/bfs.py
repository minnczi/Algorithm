import sys
sys.stdin = open('bfs_input.txt', 'r')

def BFS(s):
    visited[s] = True
    queue.append(s)
    while queue:
        target = queue.pop(0)
        travel.append(target)
        for x in AL[target]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)

T = int(input())
for tc in range(1, T+1):
    AL = [[] for _ in range(10)]
    for _ in range(9):
        s, e = map(int, input().split())
        AL[s].append(e)

    queue = []
    travel = []
    visited = [0] * 10
    BFS(1)
    print("#%d " % tc, end="")
    print(*travel[:-1])