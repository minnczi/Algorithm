lst = [0, 4, 1, 3, 1, 4, 1, 9, 9, 8]

counts_arr = [0] * 10
arr = []

for num in lst:
    counts_arr[num] += 1

for i in range(len(counts_arr)):
    arr += [i] * counts_arr[i]

print(arr)