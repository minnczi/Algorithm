submitted = [0] * 31

for _ in range(28):
    student = int(input())
    submitted[student] = 1

for i in range(1, 31):
    if not submitted[i]:
        print(i)
