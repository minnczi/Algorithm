import sys
sys.stdin = open("1959input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    if N < M:
        short, long = list(map(int, input().split())), list(map(int, input().split()))
    else:
        long, short = list(map(int, input().split())), list(map(int, input().split()))

    ll = len(long)
    sl = len(short)

    result = 0

    for i in range(ll-sl+1):
        total = 0
        for j in range(sl):
            total += short[j] * long[j+i]
        if total > result:
            result = total
    print('#%d %d' % (t, result))

