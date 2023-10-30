T = int(input())

for tc in range(1, T+1):
    # N = 원소 갯수         K = 부분 집합의 합
    N, K = map(int, input().split())
    # numbers = [i for i in range(1, 13)]
    numbers = list(range(1, 13))

    # 결과
    answer = 0
    # 모든 경우의 수에서
    for i in range(1, 1 << len(numbers)):
        # temp_sum: 합계
        # temp_count: 1의 갯수
        temp_sum = 0
        temp_count = 0
        for j in range(len(numbers)):
            if i & (1 << j):
                temp_sum += numbers[j]
                temp_count += 1
        if temp_count == N and temp_sum == K:
            answer += 1

    print('#%d %d' % (tc, answer))