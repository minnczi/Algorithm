import sys
sys.stdin = open('11605_input.txt', 'r')

T = int(input())

ops = {
    '+': (lambda a, b : a + b),
    '-': (lambda a, b : a - b),
    '*': (lambda a, b : a * b),
    '/': (lambda a, b : a / b)
    }

def calc(arr):
    stack = []
    for i in arr[0:-1]:
        if i.isdigit():
            stack.append(int(i))
        # 에러 상황 1: 중간에 .가 나온 경우
        elif i == '.':
            return 'error'
        else:
            try:
                B, A = stack.pop(), stack.pop()
                stack.append(ops[i](A, B))
            # 에러 상황 2: len(stack) <= 1인 경우
            except:
                return 'error'
    # 에러 상황 3: 마지막 연산 결과가 1개가 아닌 경우
    return 'error' if len(stack) != 1 else int(stack.pop())

for tc in range(1, T+1):
    arr = input().split()
    result = calc(arr)
    print("#%d %s" % (tc, result))

    