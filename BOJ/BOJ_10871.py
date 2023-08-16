N, X = map(int, input().split())

A = list(map(int, input().split()))
ans = list()

for num in A:
    if num < X:
        ans.append(str(num))

print(' '.join(ans))
