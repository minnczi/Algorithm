T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 1 if N % K else 0
    print("#%d %d" % (tc, result))