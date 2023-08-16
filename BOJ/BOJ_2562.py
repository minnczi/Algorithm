max_num, max_idx = 0, 0

for i in range(1, 10):
    num = int(input())
    if num > max_num:
        max_num, max_idx = num, i

print(max_num)
print(max_idx)