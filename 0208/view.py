import sys

sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    view = 0

    for i in range(2, N-2):
        local_max = 0
        current = arr[i]
        local = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        for j in local:
            if j > local_max:
                local_max = j

        # print(current, local_max)
        if current > local_max:
            view += (current-local_max)

    print("#%d %d" % (t, view))