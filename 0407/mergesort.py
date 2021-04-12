import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    a_arr = merge_sort(arr[:mid])
    b_arr = merge_sort(arr[mid:])
    temp = []
    ai = bi = 0
    while ai < len(a_arr) and bi < len(b_arr):
        if a_arr[ai] < b_arr[bi]:
            temp.append(a_arr[ai])
            ai += 1
        else:
            temp.append(b_arr[bi])
            bi += 1
    temp.extend(a_arr[ai:])
    temp.extend(b_arr[bi:])
    return temp

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print("#%d %s" % (tc, " ".join(map(str, merge_sort(arr)))))