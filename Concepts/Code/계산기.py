import sys
sys.stdin = open('calculator_input.txt', 'r')

# icp / isp 정의
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

for tc in range(1, 11):
    N = input()
    nums = input()

    # PART1: 후위표기식으로 바꾸기
    stack = []
    top = -1
    mid_exp = ""
    j = 0
    for i in nums:
        j += 1
        # 숫자: string 에 append
        if i.isdigit():
            mid_exp += i
        elif i == ")":
            while True:
                ops = stack.pop()
                top -= 1
                if ops == "(": break
                mid_exp += ops

        # 연산자: top보다 우선순위가 같거나 높으면 stack에 append
        # 우선순위가 낮으면, 우선순위가 같거나 높은 연산자가 나올때까지 pop
        else:
            if top < 0 or icp[i] >= isp[stack[top]]:
                pass
            else:
                while stack and icp[i] < isp[stack[top]]:
                    mid_exp += stack.pop()
                    top -= 1
            stack.append(i)
            top += 1
    while stack:
        mid_exp += stack.pop()
        top -= 1
    
    # PART2: 변환된 식을 가지고 스택을 이용하여 계산
    stack2 = []
    ops = {
        "+": (lambda a,b: a+b),
        "-": (lambda a,b: a-b),
        "*": (lambda a,b: a*b),
        "/": (lambda a,b: a/b)}
    for i in mid_exp:
        if i.isdigit():
            stack2.append(int(i))
        else:
            B = stack2.pop()
            A = stack2.pop()
            result = ops[i] (A,B)
            stack2.append(result)
    
    print("#%d %d" % (tc, stack2[0]))
