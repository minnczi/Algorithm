T = int(input())

for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    total = 0

    for n in range(N):
        damage = D * (1+n*L*0.01)
        total += damage
    
    print("#%d %d" % (tc, total))
