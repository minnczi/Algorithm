T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    # N이 홀수인 경우
    # 예를들어 N이 5면 -1이 두번 반복되고 5가 더해짐
    if N % 2:
        result = (N//2)*(-1) + N
    else:
        result = (N//2)*(-1)

    print(f'#{test_case} {result}')