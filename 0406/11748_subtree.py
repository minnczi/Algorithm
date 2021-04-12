import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def find_nodes(n):
    global cnt
    cnt += 1
    if ch1[n]:
        find_nodes(ch1[n])
    if ch2[n]:
        find_nodes(ch2[n])
    return
    

for tc in range(1, T+1):
    cnt = 0
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    # 트리 만들기
    for i in range(E):
        parent = edges[2*i]
        child = edges[2*i+1]
        if ch1[parent]:
            ch2[parent] = child
        else:
            ch1[parent] = child
    
    find_nodes(N)
    print("#%d %d" % (tc, cnt))