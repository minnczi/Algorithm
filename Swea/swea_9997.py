T = int(input())

for tc in range(1, T+1):
    theta = int(input())
    h, m = divmod(theta, 30)
    print("#%d %d %d" % (tc, h, m*2))