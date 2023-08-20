import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
pa = [0] * (N+1)
pa[1] = 1
visited = [0] * (N+1)
visited[1] = 1
queue = []

def find_parent(a, b): 
    if visited[a]:
        parent, child = a, b
        pa[child] = parent
    elif visited[b]:
        parent, child = b, a
        pa[child] = parent
    else:
        queue.append([a, b])
    visited[a] = visited[b] = 1
    

for i in range(N-1):
    a, b = map(int, input().split())
    find_parent(a, b)
    if queue:
        for _ in range(len(queue)):
            a, b = queue.pop(0)
            find_parent(a, b)
    

for i in range(2, N+1):
    print(pa[i])