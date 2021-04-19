# SWEA 11906 퀵정렬
def quicksort(left, right):
    if left >= right:
        return
    
    i = j = left
    for _ in range(right-left):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    
    arr[i], arr[right] = arr[right], arr[i]
    quicksort(left, i-1)
    quicksort(i+1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(0, N-1)
    print("#%d %d" % (tc, arr[N//2]))