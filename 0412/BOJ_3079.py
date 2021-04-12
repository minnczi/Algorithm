import sys
input = sys.stdin.readline

N, M = map(int, input().split())
line = [int(input()) for _ in range(N)]
s, e = 0, max(line)*M

ans = 0
while s <= e:
    mid = (s+e) // 2
    t = sum([mid//i for i in line])
    if t >= M:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1 
print(ans)