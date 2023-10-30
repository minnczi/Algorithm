T = int(input())

def enque(x):
    global rear
    if rear >= len(queue):
        print("Overflow!")
        return
    rear += 1
    queue[rear] = x

def deque():
    global front
    if front == rear:
        print("Underflow!")
        return
    front += 1
    print(queue[front], end=" ")

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # queue 초기화
    queue = [0] * len(arr)
    front = rear = -1

    for x in arr:
        enque(x)
    
    print("#%d" % tc, end=" ")
    for _ in range(len(queue)):
        deque()
    