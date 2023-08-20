# 11907. 이진 탐색
import sys
sys.stdin = open('input.txt', 'r')

# dirc는 직전에 탐색했던 방향을 나타내는 변수
# 0은 왼쪽, 1은 오른쪽
def binary_search(start, end, dirc):
    global cnt
    if start > end:
        return
    mid = (start+end) // 2
    if A[mid] in B:
        cnt += B_cnt[A[mid]]
    if start == end:
        return
    # 직전에 오른쪽을 탐색했을 경우, 다음번 재귀에서는 왼쪽만 탐색하면 됨
    if dirc:
        binary_search(start, mid-1, 0)
    # 작전에 왼쪽을 탐색했을 경우
    else:
        binary_search(mid+1, end, 1)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B_cnt = {}
    for key in B:
        B_cnt[key] = B_cnt.get(key, 0) + 1
    B = set(B)
    
    start = 0
    end = len(A)-1
    mid = end // 2
    cnt = 1 if A[mid] in B else 0
    binary_search(start, mid-1, 0)
    binary_search(mid+1, end, 1)
    print("#%d %d" % (tc, cnt))