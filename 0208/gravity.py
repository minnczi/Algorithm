import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    max = 0
    height = 0

    # print(D)
    # 리스트의 각 원소마다
    for i in range(N):
        height = 0
        # 뒤에 오는 숫자들과 비교
        for j in range(i+1, N):
            # print(D[i], j)
            # 만약 뒤에 오는 숫자(j)가 현재숫자(D[i]) 보다 작다면, 떨어질 공간이 있다는 거니까 그만큼 떨어지는 height가 1씩 증가
            if D[i] > D[j]:
                height += 1
        # 만약 총 떨어지는 높이 height가 현재 max보다 크다면 max를 height로 대체
        if height > max:
            max = height

    print('#%d %d' % (t, max))