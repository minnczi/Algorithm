import sys
sys.stdin = open('0331_input.txt', 'r')

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

# 합이 k가 되는 경우의 수를 담을 배열
# dp[0] = 1 => 합이 0이 되는 경우의 수는 1개
dp = [0 for i in range(K+1)]
dp[0] = 1

for i in coins:
    for j in range(i, K+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[K])