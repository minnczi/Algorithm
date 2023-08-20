import sys
sys.stdin = open('node_input.txt', 'r')

T = int(input())

def BFS(start, end):
    queue = [start]
    dist = [0] * (V+1)

    while queue:
        current = queue.pop(0)
        new_dist = dist[current] + 1
        for node in AL[current]:
            if node == end:
                return new_dist
            if not dist[node]:
                dist[node] = new_dist
                queue.append(node)
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        AL[start].append(end)
        AL[end].append(start)
    S, E = map(int, input().split())
    result = BFS(S, E)
    print("#%d %d" % (tc, result))