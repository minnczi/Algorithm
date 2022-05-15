# BOJ_6137 문자열 생성

N = int(input())
letters = [input() for _ in range(N)]
T = ''
F, B = 0, N-1
stack = []
temp = 0

while True:
    if B <= F:
        if not stack:
            break
        else:
            continue

    if letters[F] == letters[B]:
        stack.append(letters[F])
        F, B = F+1, B-1
        continue
    
    
    while stack:
        temp = len(stack)
        T += stack.pop(0)
    
    if letters[F] <= letters[B]:
        T += letters[F]
        F, B = F+1, B+temp
    else:
        T += letters[B]
        F, B = F-temp, B-1
    temp = 0

T += letters[F]
print(T)