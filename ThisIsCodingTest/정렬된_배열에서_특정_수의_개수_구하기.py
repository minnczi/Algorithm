"""
입력
7 2
1 1 2 2 2 2 3

출력
4
"""
N, x = map(int, input().split())
num_list = list(map(int, input().split()))

left = 0
right = N-1
mid = (left + right) // 2

# 가장 첫 x가 나오는 지점 찾기
while left <= right:
    mid = (left + right) // 2
    print(left, right, mid)
    if mid >= x:
        right = mid - 1
    else:
        left = mid + 1

print(mid)
    
# pivot을 기준으로 왼쪽 

