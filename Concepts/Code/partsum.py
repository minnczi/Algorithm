def partsum(level, start, total):
    # 종료조건 1: level >= N
    if level >= N:
        global cnt
        if total == K: cnt += 1
        return
    
    # 종료조건 2: total >= K (가지치기)
    elif total >= K:
        return
    
    for i in range(start, 13 - N + level):
        partsum(level+1, i+1, total+i)
        

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    partsum(0, 1, 0)
    print("#%d %d" % (tc, cnt))