A = list(range(1, 13))
N = 12
subset = [0] * N

def DFS_subset(level, S, C):
    if S > K or C > N:
        return

    if level == N:
        if C == M and S == K:
            global ans
            ans += 1
        return

    subset[level] = 1
    DFS_subset(level+1, S+A[level], C+1) 
    subset[level] = 0
    DFS_subset(level+1, S, C)

T = int(input())
for tc in range(1, T+1):
    M, K = map(int, input().split())
    ans = 0
    cnt = 0
    DFS_subset(0, 0, 0)
    print("#%d %d" % (tc, ans))
