# swea 5099
# 영주님 코드 보고 재작성 한 코드
import sys
sys.stdin = open('5099_input.txt', 'r')

T = int(input())

# cheese에는 치즈의 양이, queue에는 오븐에 있는 피자의 인덱스 넘버가 저장되있음
# queue에 있는 인덱스로 치즈 양을 찾을수 있으니 queue에는 따로 치즈양을 저장할 필요가 없음
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = [i for i in range(N)]
    temp = N
    
    while len(queue) > 1:
        i = queue.pop(0)
        cheese[i] //= 2
        if cheese[i] != 0:
            queue.append(i)
            
        elif temp < M:
            queue.append(temp)
            temp += 1
    print("#%d %d" % (tc, queue[0]+1))
