import sys
sys.stdin = open('hamburger_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    toppings = []
    for _ in range(N):
        toppings.append(list(map(int, input().split())))
    
    best = 0
    for i in range(1 << N):
        score = cal = 0
        for j in range(N):
            if i & (1 << j):
                score += toppings[j][0]
                cal += toppings[j][1]
        if score > 0 and cal <= L:
            print(i)
            print(cal, score)
            best = score
    
    print(score)