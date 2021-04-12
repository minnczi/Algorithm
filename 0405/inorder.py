# 트리의 중위순회
import sys
sys.stdin = open('inorder_input.txt', 'r')


def inorder(n):
    if n*2 <= N:
        inorder(n*2)
    print(tree[n], end="")
    if n*2+1 <= N:
        inorder(n*2+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        info = input().split()
        tree[int(info[0])] = info[1]
    
    print("#%d" % tc, end=" ")
    inorder(1)
    print("")




    
