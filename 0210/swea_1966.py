import sys

sys.stdin = open("input.txt", "r")

T = int(input())

# counting sort
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    counts = [0] * 51

    for i in arr:
        counts[i] += 1

    sorted_list = []
    for i in range(0, 51):
        sorted_list += [str(i)] * counts[i]

    sorted_str = " ".join(sorted_list)
    print('#%d %s' % (t, sorted_str))