N = int(input())
town = sorted(list(map(int, input().split())))

if N % 2:
    print(town[N//2])
else:
    print(town[N//2-1])
