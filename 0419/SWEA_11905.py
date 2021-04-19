# SWEA 11905 병합정렬
def mergesort(arr):
    global cnt
    if len(arr) == 1:
        return arr

    # arr의 길이가 1이 될때까지 반으로 나누기
    mid = len(arr) // 2
    a = mergesort(arr[:mid])
    b = mergesort(arr[mid:])
    # 리스트 병합 전 왼쪽 max가 오른쪽 max보다 큰 경우 cnt+1
    if a[-1] > b[-1]:
        cnt += 1

    # 나누어 정렬된 두개의 리스트를 병합하기
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = mergesort(arr)
    print("#%d %d %s" % (tc, sorted_arr[N//2], cnt))