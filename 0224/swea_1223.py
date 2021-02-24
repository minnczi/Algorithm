import sys
sys.stdin = open('calculator_input.txt', 'r')

for tc in range(1, 11):
    N = input()
    nums = input()

    # PART1: 후위표기식으로 바꾸기
    order = {"+": 1, "*": 2}
    stack = []
    top = -1
    mid_exp = ""
    for i in nums:
        if i.isdigit():
            mid_exp += i
        else:
            if top < 0 or order[i] >= order[stack[top]]:
                pass
            else:
                while stack and order[i] < order[stack[top]]:
                    mid_exp += stack.pop()
                    top -= 1
            stack.append(i)
            top += 1

    while stack:
        mid_exp += stack.pop()
        top -= 1
    
    # PART2: 변환된 식을 가지고 스택을 이용하여 계산
    stack2 = []
    ops = {"+": (lambda a,b: a+b), "*": (lambda a,b: a*b)}
    for i in mid_exp:
        if i.isdigit():
            stack2.append(int(i))
        else:
            B = stack2.pop()
            A = stack2.pop()
            result = ops[i] (A,B)
            stack2.append(result)
    
    print("#%d %d" % (tc, stack2[0]))
