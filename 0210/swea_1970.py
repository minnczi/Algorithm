import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
wons = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    money = int(input())
    result = ['0'] * 8

    for i in range(0, 8):
        cnt, change = divmod(money, wons[i])
        result[i] = str(cnt)
        money = change
    
    print("#%d" % t)
    print(" ".join(result))