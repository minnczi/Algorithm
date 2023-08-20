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