import sys
sys.stdin = open('1940_input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    seconds = int(input())
    speed = 0
    dist = 0

    for sec in range(seconds):
        action = list(map(int, input().split()))
        if action[0] == 1:
            speed += action[1]
        elif action[0] == 2:
            speed -= action[1]
            if speed < 0:
                speed = 0
        dist += speed
    
    print('#%d %d' % (tc, dist))

