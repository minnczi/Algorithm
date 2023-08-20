import sys
sys.stdin = open('9839_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    best = -1
    for i in range(N-1):
        for j in range(i, N):
            temp = arr[i] * arr[j]
            if temp <= best:
                continue
            temp = str(temp)
            for k in range(len(temp)-1):
                if int(temp[k])+1 != int(temp[k+1]):
                    break
            else:
                best = int(temp)
    
    print("#%d %d" % (tc, best))