N = int(input())
nums = list(map(int, input().split()))

start, end = 0, N-1
fp = -1

while start <= end:
    mid = (start + end) // 2
    if nums[mid] == mid:
        fp = mid
        break
    elif nums[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1

print(fp)