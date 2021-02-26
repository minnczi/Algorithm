import sys
sys.stdin = open('hw_input.txt', 'r')

N = 10
for _ in range(N):
    # testcase and number of edges
    tc, E = map(int, input().split())

    # edge 데이터 받아서 adjacent list 만들기
    arr = list(map(int, input().split()))
    AL = [[] for _ in range(100)]

    for i in range(0, len(arr), 2):
        AL[arr[i]].append(arr[i+1])
    
    stack = [0]
    visited = [0] * 100

    while stack:
        current = stack.pop()
        visited[current] = 1

        for i in AL[current]:
            if not visited[i]:
                stack.append(i)
    
    result = 1 if visited[99] else 0
    print("#%d %d" % (tc, result))

