# SWEA 11908 부분집합의 합
def powerset_sum(arr, start, subtotal):
    global cnt
    if subtotal == M:
        cnt += 1
        return
    if subtotal >= M:
        return
    for i in range(start, N):
        subtotal += arr[i]
        powerset_sum(arr, i+1, subtotal)
        subtotal -= arr[i]
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    powerset_sum(arr, 0, 0)
    print("#%d %d" % (tc, cnt))