def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    a_arr = merge_sort(arr[:mid])
    b_arr = merge_sort(arr[mid:])
    temp = []
    ai = bi = 0
    while ai < mid and bi < mid:
        if a_arr[ai] < b_arr[bi]:
            temp.append(a_arr[ai])
            ai += 1
        else:
            temp.append(b_arr[bi])
            bi += 1
    temp.extend(a_arr[ai:])
    temp.extend(b_arr[bi:])
    return temp

print(merge_sort([1, 3, 2, 4]))