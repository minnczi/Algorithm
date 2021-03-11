import sys
sys.stdin = open('1225_input.txt', 'r')

for _ in range(10):
    tc = input()
    queue = list(map(int, input().split()))
    
    arr = [1, 2, 3, 4, 5]
    i = 0
    while queue[-1] != 0:
        current = queue.pop(0) - arr[i%5]
        if current < 0:
            current = 0
        queue.append(current)
        i += 1
    
    print("#%s" % tc, end=" ")
    print(*queue)