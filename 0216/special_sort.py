import sys
sys.stdin = open('sample_input_sort.txt', 'r')

def find_max(arr):
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def find_min(arr):
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(10):
        # 짝수번째 인덱스에서는 max 찾기
        if i % 2 == 0:
            max_idx = find_max(numbers[i:]) + i
            # max와 현재 숫자 스왑하기
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
        # 홀수번째 인덱스에서는 min 찾기
        else:
            min_idx = find_min(numbers[i:]) + i
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    result = " ".join(list(map(str, numbers[0: 10])))
    print("#%d %s" % (tc, result))