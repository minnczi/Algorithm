# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    N = int(input())
    map = [[0] + list(map(int, input().split())) for _ in range(N)]
    map.insert(0,[0]*(N+1))

    DP = [[1000000] + [0]*(N) for _ in range(N)]
    DP.insert(0,[1000000] * (N+1))
    DP[0][1] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            DP[i][j] = map[i][j] + min(DP[i-1][j], DP[i][j-1])
    
    print(DP[N][N])