arr = [55, 7, 78, 12, 42]

for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        print(i, j)
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
