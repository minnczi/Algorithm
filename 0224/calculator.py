import sys
sys.stdin = open('calculator_input.txt', 'r')

for tc in range(1, 11):
    order = {"+": 1, "*": 2}
    nums = input()

    stack = []
    top = -1
    mid_exp = ""
    for i in nums:
        if i.isdigit():
            mid_exp += i
        else:
            print(i, order[i], top)
            if top < 0 or order[i] >= order[top]:
                pass
            else:
                while stack and order[i] < order[top]:
                    mid_exp += stack.pop()
                    top -= 1
            stack.append(i)
            top += 1
            print(stack, top)

    while stack:
        mid_exp += stack.pop()
        top -= 1
    
    print(mid_exp)
