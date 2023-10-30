import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

stars = [0] * (N+1)
far_lines = []
for _ in range(M):
    # row = list(map(int, input().split()))
    # print(row)
    x, y, z = map(int, input().split())
    if abs(x-y) == 1:
        stars[x] = 1
        stars[y] = 1
    else:
        far_lines.append([x, y])

circle_cnt = 0
line_cnt = 0
for x, y in far_lines:
    left = min(x, y)
    right = max(x, y)
    if 0 not in stars[left:right+1]:
        for i in range(left, right+1):
            stars[i] = 0
        circle_cnt += 1

if 1 not in stars:
    line_cnt = 0
else:
    prev = stars.index(1)
    for i in range(prev+1, len(stars)):
        if stars[i] == 0:
            if prev == 1:
                line_cnt += 1
        prev = stars[i]

    if prev == 1:
        line_cnt += 1

print(1, abs(circle_cnt-line_cnt))
