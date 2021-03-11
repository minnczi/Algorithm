import sys
sys.stdin = open('1225_input.txt', 'r')

key = [1, 2, 3, 4, 5]
def password(queue):
    i = 0
    while True:
        current = queue.pop(0) - key[i%5]
        queue.append(current)
        if current <= 0:
            queue[-1] = 0
            return(queue)
        i += 1

for _ in range(10):
    tc = input()
    queue = list(map(int, input().split()))
    result = password(queue)
    print("#%s" % tc, *result)