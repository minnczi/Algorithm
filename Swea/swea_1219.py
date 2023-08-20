import sys
sys.stdin = open('1219_input.txt', 'r')

for _ in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    AL = [[] for _ in range(100)]

    for i in range(0, N*2, 2):
        AL[arr[i]].append(arr[i+1])
    
    visited = [0] * 100
    queue = [0]
    while queue:
        current = queue.pop()
        visited[current] = 1
        for i in AL[current]:
            if not visited[i] and i not in queue:
                queue.append(i)
    print("#%d %d" % (tc, visited[99]))