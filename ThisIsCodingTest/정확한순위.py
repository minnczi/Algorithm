N, M = map(int, input().split())
INF = 1e9
rank = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    rank[a][b] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                rank[a][b] = 0
                continue
            rank[a][b] = min(rank[a][b], rank[a][k]+rank[k][b])

ans = 0
for a in range(1, N+1):
    cnt = 0
    for b in range(1, N+1):
        if rank[a][b] < INF or rank[b][a] < INF:
            cnt += 1
    if cnt == N:
        ans += 1

print(ans)