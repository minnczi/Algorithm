import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N):
        if M % 2 == 0:
            switch = "OFF"
            break
        M = M // 2
    else:
        switch = "ON"
    
    print("#%d %s" % (tc, switch))
    