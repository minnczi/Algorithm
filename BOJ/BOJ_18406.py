num = input()

sum_front = sum(list(map(int, num[:len(num)//2])))
sum_back = sum(list(map(int, num[len(num)//2:])))

if sum_front == sum_back:
    print("LUCKY")
else:
    print("READY")