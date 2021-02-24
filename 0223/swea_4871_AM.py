import sys
sys.stdin = open('4871_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # Adjacent Matrix 만들기
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
    
    # 문제에서 찾아야하는 경로의 시작점과 끝점
    start, end = map(int, input().split())

    # DFS 구현
    stack = [start]
    visited = [0] * (V+1)
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = 1
        for i in range(V+1):
            if arr[current][i] == 1 and not visited[i]:
                stack.append(i)
    
    result = 1 if visited[end] == 1 else 0
    print("#%d %d" % (tc, result))