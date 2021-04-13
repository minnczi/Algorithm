T = int(input())

for tc in range(1, T+1):
    N = float(input())
    bi = ''
    for i in range(1, 13):
        if N == 0:
            break
        if N >= (1/(1<<i)):
            bi += '1'
            N -= (1/(1<<i))
        else:
            bi += '0'
    else:
        bi = 'overflow'
    print("#%d %s" % (tc, bi))