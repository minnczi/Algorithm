import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def reverse_map(lst):
    return list(reversed(lst))


for t in range(1, T+1):
    N = int(input())
    square = []

    for _ in range(N):
        square.append(list(map(str, input().split())))
    
    square_90 = list(map(reverse_map, list(zip(*square))))
    square_180 = list(map(reverse_map, list(zip(*square_90))))
    square_270 = list(map(reverse_map, list(zip(*square_180))))

    print('#%d' % t)
    for i in range(N):
        print("".join(square_90[i]), end=" ")
        print("".join(square_180[i]), end=" ")
        print("".join(square_270[i]))
