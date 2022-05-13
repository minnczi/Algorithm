INF = 1e9
N = int(input())
buses = [[INF]*(N+1) for _ in range(N+1)]

# 처음 인풋 값 받기
for i in range(int(input())):
    a, b, c = map(int, input().split())
    buses[a][b] = min(buses[a][b],c)

# 플로이드 워셜
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                buses[i][j] = 0
            else:
                buses[i][j] = min(buses[i][j], buses[i][k] + buses[k][j])

for r in range(1, N+1):
    for c in range(1, N+1):
        print(buses[r][c], end=" ")
    print()
