import sys
sys.stdin = open('sample_input.txt', 'r')

def search_binary(page, target):
    l, r = 1, page
    answer = 0
    while True:
        answer += 1
        mid = (l + r) // 2
        if target == mid:
            return answer
        elif target > mid:
            l = mid
        else:
            r = mid

def find_winner(a, b):
    if a == b:
        return 0
    return 'A' if a < b else 'B'

T = int(input())
for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    
    a_bin = search_binary(p, a)
    b_bin = search_binary(p, b)

    print("#%d %s" % (tc, find_winner(a_bin, b_bin)))

