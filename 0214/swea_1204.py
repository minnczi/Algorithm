import sys
sys.stdin = open('1204_input.txt', 'r')

T = int(input())

for _ in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    count = [0] * 101
    max_idx = 0

    for i in scores:
        count[i] += 1
        if count[i] > count[max_idx]:
            max_idx = i
        elif count[i] == count[max_idx] and i > max_idx:
            max_idx = i
    
    print("#%d %d" % (tc, max_idx))