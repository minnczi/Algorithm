import sys
sys.stdin = open('ex02_input.txt', 'r')

T = int(input())

def if_zero(numbers, n):
    # 각 경우의 수 i 마다
    for i in range(1, 1 << n):
        temp = 0
        # i의 각 자리수를 0001(1<<0 <- j), 0010(1<<1), 0100(1<<2), 1000(1<<3)과 비교
        for j in range(n):
            # j와 비교했을때 해당 자리수도 1인 경우
            if i & (1 << j):
                # 1이라면 j번째 자리수에 해당하는 element가 존재! --> numbers[j]를 temp에 더해준다
                temp += numbers[j]
        if temp == 0:
            return 1
    else:
        return 0
    

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    n = 10 
    result = if_zero(numbers, n)
    print("#%d %d" % (tc, result))