import sys
sys.stdin = open('inorder_input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    AL = [0 for _ in range(N+1)]
    for _ in range(N):
        i, alpha, left, right = input().split()
        AL[int(i)] = [alpha, int(left), int(right)]

    print(AL)