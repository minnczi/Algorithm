N = int(input())

def is_ps(PS):
    stack = 0
    for p in PS:
        if p == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                return 'NO'
    return 'YES' if stack == 0 else 'NO'

for _ in range(N):
    PS = []
    PS.extend(input())
    
    print(is_ps(PS))