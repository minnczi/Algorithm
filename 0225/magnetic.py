import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(zip(*arr))
    
    cnt = 0
    for row in arr:
        flag = 0
        for col in row:
            if col == 1:
                flag = 1
            elif col == 2 and flag:
                cnt += 1
                flag = 0
    print("#%d %d" % (tc, cnt))