def NQueen(r):
    global cnt
    if r == N:
        cnt += 1
        return
    for c in range(N):
        if vr[c] | vd1[r+c] | vd2[r-c+N-1]:
            continue
        vr[c] = vd1[r+c] = vd2[r-c+N-1] = 1
        NQueen(r+1)
        vr[c] = vd1[r+c] = vd2[r-c+N-1] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    vr = [0] * N
    vd1 = [0] * (N*2-1)
    vd2 = [0] * (N*2-1)
    cnt = 0
    NQueen(0)
    print("#%d %d" % (tc, cnt))
