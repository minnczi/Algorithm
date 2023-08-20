import sys
sys.stdin = open('input.txt', 'r')

ops = {
    '+': (lambda a,b: a+b),
    '-': (lambda a,b: a-b),
    '*': (lambda a,b: a*b),
    '/': (lambda a,b: a/b)
}


def calculate(n):
    if isinstance(tree[n], list):
        a = calculate(int(tree[n][1]))
        b = calculate(int(tree[n][2]))
        tree[n] = ops[tree[n][0]](a, b)
    return tree[n]

    

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        temp = list(input().split())
        if len(temp) == 2:
            tree[int(temp[0])] = int(temp[1])
        else:
            tree[int(temp[0])] = temp[1:]
    calculate(1)
    print("#%d %d" % (tc, int(tree[1])))