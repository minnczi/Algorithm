import sys
sys.stdin = open('4871_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # adjacent list 초기화
    arr = [[] for _ in range(V+1)]
    # adjacent list에 input 받기
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)
    
    # 문제에서 찾아야하는 경로의 시작점과 끝점
    start, end = map(int, input().split())

    # 접근법: start에서부터 dfs 찾기를 실시해서,
    # 끝났을때 visited[end]가 1이라면 경로 있음, 아니면 경로 없음
    stack = [start]
    visited = [0] * (V+1)
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = 1
        for i in arr[current]:
            if not visited[i]:
                stack.append(i)
    
    result = 1 if visited[end] == 1 else 0
    print("#%d %d" % (tc,result))