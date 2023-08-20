import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    stops = [0] * 5001

    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            stops[i] += 1

    P = int(input())
    buses = [stops[int(input())] for _ in range(P)]

    print('#%d %s' % (t, " ".join(map(str, buses))))