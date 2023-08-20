import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    fh, fm, sh, sm = map(int, input().split())

    roundup, minute = divmod((fm+sm), 60)
    hour = (fh + sh + roundup) % 12

    if hour == 0:
        hour = 12

    print('#%d %d %d' % (t, hour, minute))