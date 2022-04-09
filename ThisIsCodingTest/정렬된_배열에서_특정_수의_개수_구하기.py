"""
입력
7 2
1 1 2 2 2 2 3

출력
4
"""
N, x = map(int, input().split())
num_list = list(map(int, input().split()))

def find_left_key():
    left = 0
    right = N-1
    key = -1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] >= x:
            right = mid - 1
            if num_list[mid] == x:
                key = mid
        else:
            left = mid + 1
    return key

def find_right_key(key):
    left = key
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] <= x:
            left = mid + 1
            if num_list[mid] == x:
                key = mid
        else:
            right = mid - 1
    return key

left_key = find_left_key()

if left_key == -1:
    print(left_key)
else:
    right_key = find_right_key(left_key)
    print(right_key - left_key + 1)
