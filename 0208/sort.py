import sys

sys.stdin = open("input.txt", "r")

T = int(input())

# counting sort
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    counts = [0] * 51

    for i in arr:
        counts[i] += 1

    sorted_list = []
    for num in arr:
        pass
                

