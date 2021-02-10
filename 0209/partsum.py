import sys
sys.stdin = open('sample_input_sum.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_sum = max_sum = current = arr[0] + arr[1] + arr[2]

    for idx in range(0, N-M):
        current = current - arr[idx] + arr[idx+M]

        if current > max_sum:
            max_sum = current
        elif current < min_sum:
            min_sum = current

    result = max_sum - min_sum
    print('#%d %d' % (t, result))
