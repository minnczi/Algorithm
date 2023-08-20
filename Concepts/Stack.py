# v를 stack의 맨 뒤에 추가한다
def push(v):
    stack.append(v)

def pop(v):
    stack.pop()

def push2(v):
    global top
    # overflow 확인
    # 조건문 작성
    if top >= len(stack)-1:
        print("Stack Overflow")
        return 1 
    top += 1
    stack[top] = v

def pop2():
    global top
    # underflow 확인
    # 조건문 작성 
    if top < 0:
        print("Stack Underflow")
        return -1
    x = stack[top]
    top -= 1

top = -1
N = 5
stack = [""] * N
push2(1)
push2(2)
push2(2)
push2(2)
push2(2)
push2(2)
pop2()
pop2()
pop2()
pop2()
pop2()
pop2()

