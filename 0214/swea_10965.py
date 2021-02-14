T = int(input())

for tc in range(1, T+1):
    A = int(input())

    for num in range(1, A+1):
        if ((num * A) ** (1/2)) == int((num * A) ** (1/2)):
            result = num
            break
    
    print("#%d %d" % (tc, result))