# SWEA 전자카트
import sys
sys.stdin = open('input.txt', 'r')

def perm(k):
    global min_cost
    if k >= N:
        cost = 0
        for i in range(N):
            cost += costs[i][order[i]]
        if cost < min_cost:
            min_cost = cost
        return
    for i in range(k, N):
        order[i], order[k] = order[k], order[i]
        perm(k+1)
        order[i], order[k] = order[k], order[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1000000000
    order = list(range(N))
    perm(0)
    print("#%d %d" % (tc, min_cost))

