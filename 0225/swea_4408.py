import sys
sys.stdin = open('4408_input.txt', 'r')

T = int(input())
 
for tc in range(1, T+1):
    hallway = [0] * 200
     
    N = int(input())
    for _ in range(N):
        s, e = map((lambda x: int(x)-1), input().split())
        if e < s:
            s, e = e, s
        for i in range(s//2, e//2+1):
            hallway[i] += 1
     
    print("#%d %d" % (tc, max(hallway)))
    