import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())

checkpoint_pos = []
checkpoint_neg = []


for _ in range(N):
    x = int(input())
    if x >= 0:
        checkpoint_pos.append(x)
    else:
        checkpoint_neg.append(-x)

checkpoint_pos.sort()
checkpoint_neg.sort()


def find_min_dist(lst):
    idx = len(lst) - 1

    dist = 0
    while idx >= 0:
        dist += lst[idx] * 2
        idx -= K

    return dist


print(find_min_dist(checkpoint_pos) + find_min_dist(checkpoint_neg))
