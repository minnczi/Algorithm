import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())

    arr = ['0'] * N
    for task_num in range(1, Q+1):
        left, right = map(int, input().split())
        for idx in range(left-1, right):
            arr[idx] = str(task_num)

    result = " ".join(arr)
    print("#%d %s" % (t, result))