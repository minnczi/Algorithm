T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    data = a ** b
    print(data % 11)