# 1966. 숫자를 정렬하자
def selection_sort(arr, n):
    min_num = arr[n]
    for i in range(n+1, N):
        if arr[i] < min_num:
            arr[n], arr[i] = arr[i], min_num
            min_num = arr[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for n in range(N-1):
        selection_sort(arr, n)
    print("#%d %s" % (tc, " ".join(map(str, arr))))