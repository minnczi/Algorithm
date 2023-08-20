import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tasks = sorted([list(map(int, input().split())) for _ in range(N)], key=(lambda x: x[1]))
    
    cnt = 1
    task_end = tasks[0][1]
    for task in tasks:
        if task[0] >= task_end:
            cnt += 1
            task_end = task[1]
    print("#%d %d" % (tc, cnt))    