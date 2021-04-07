n, k = map(int, input().split())

coins = []

for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

N = len(coins)
cnt = 0
for i in range(1 << N):
    temp = 0
    for j in range(N):
        if i & (1 << j):
            temp += coins[j]
    if temp == k:
        cnt += 1
print(cnt)