import sys
sys.stdin = open('password_input.txt', 'r')

for tc in range(1, 11):
    N, password = input().split()
    stack = []
    top = -1

    for num in password:
        if top == -1 or stack[top] != num:
            stack.append(num)
            top += 1
        else:
            # 마지막 글자 잘라내기
            stack.pop()
            top -= 1
    print("#%d %s" % (tc, "".join(stack)))