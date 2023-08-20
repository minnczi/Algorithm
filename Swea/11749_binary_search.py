import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def inorder(idx):
    global num
    if idx*2 > N:
        tree[idx] = num
        num += 1
        return
    
    if idx*2 <= N:
        inorder(idx*2)
    tree[idx] = num
    num += 1
    if idx*2 + 1 <= N:
        inorder(idx*2+1)

for tc in range(1, T+1):
    num = 1
    N = int(input())
    tree = [0] * (N+1)
    inorder(1)
    print("#%d %d %d" % (tc, tree[1], tree[N//2]))