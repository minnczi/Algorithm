# BOJ_12865 평범한 배낭
# knapsack algorithm
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
items.insert(0, [0,0])

# DP[n][k] = 최대 n개의 물건으로 k의 무게를 만들었을때 나올수 있는 가치의 최댓값
# DP[2][8] = 최대 2개의 물건을 넣어 무게가 8이 되는 경우의 수 중 가치의 최댓값
DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):    
        w = items[i][0]
        v = items[i][1]

        if j < w:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-w]+v)

print(DP[N][K])