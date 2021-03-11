import sys
sys.stdin = open('10580_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    lines = []
    ans = 0

    N = int(input())

    for _ in range(N):
        s1, e1 = map(int, input().split())
        for s2, e2 in lines:
            if (s1 > s2) ^ (e1 > e2):
                ans += 1
        lines.append([s1, e1])
    print("#%d %d" % (tc, ans))