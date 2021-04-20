# SWEA 전자카트
import sys
sys.stdin = open('input.txt', 'r')

def perm(k, n):
    if k == n:
        global min_cost
        temp = 0
        for i in range(n):
            temp += cost[order[i]][order[i+1]]
        if temp < min_cost:
            min_cost = temp
    else:
        for i in range(k, n):
            order[k], order[i] = order[i], order[k]
            perm(k+1, n)
            order[k], order[i] = order[i], order[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    order = list(range(1, N+1)) + [1] # 방문 순서    
    cost = [[0] + list(map(int, input().split())) for _ in range(N)] # 배터리 비용 배열
    cost.insert(0, [0 * (N+1)])
    min_cost = 10001 # 최소 비용
    perm(1, N)
    print("#%d %d" % (tc, min_cost))

