N = int(input())
N = N*10 if N < 10 else N

num = N
cycle = 0
while True:
    digit_sum = num//10 + num%10
    num = (num%10) * 10 + digit_sum%10
    cycle += 1

    if num == N:
        break

print(cycle)
