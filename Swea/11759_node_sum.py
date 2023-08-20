# 11759 노드의 합
import sys
sys.stdin = open('input.txt', 'r')

def tree_sum(n):
    if n > N:
        return 0
    elif tree[n] != 0:
        return tree[n]
    return tree_sum(2*n) + tree_sum(2*n+1)

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    
    print("#%d %d" % (tc, tree_sum(L)))
