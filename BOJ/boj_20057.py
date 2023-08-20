import sys
import math

sys.stdin = open('20057_input.txt', 'r')

N = int(input())
arr = [[0]*(N+4)] * 2
arr += [[0, 0] + list(map(int, input().split())) + [0, 0] for _ in range(N)]
arr += [[0]*(N+4)] * 2


# N NE E SE S SW W NW 순서
dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
# 움직일 순서 W S E N
move = [6, 4, 2, 0]
# 현재 위치
r = c = (N // 2) + 2 
# 토네이도가 부는 방향 (현재 동쪽에서 서쪽으로 불고 있으니 W부터 시작)
tornado = 0

# i = 한쪽 방향으로 움직일 칸 수
for i in range(1, N):
    loop = 3 if i == N-1 else 2
    for _ in range(loop):
        for _ in range(i):
            d = move[tornado%4]
            # 토네이도 위치 이동
            r += dxy[d][0]
            c += dxy[d][1]
            sand = arr[r][c]
            temp_sum = 0
            for row in arr:
                temp_sum += sum(row)
            arr[r][c] = 0
            # 모래 이동 (대각선 앞쪽)
            arr[r+dxy[(d+1)%8][0]][c+dxy[(d+1)%8][1]] = math.floor(arr[r+dxy[(d+1)%8][0]][c+dxy[(d+1)%8][1]] + (sand * 0.1))
            arr[r+dxy[(d+7)%8][0]][c+dxy[(d+7)%8][1]] = math.floor(arr[r+dxy[(d+7)%8][0]][c+dxy[(d+7)%8][1]] + (sand * 0.1))
            # 모래 이동 (양옆 또는 위아래)
            arr[r+dxy[(d+2)%8][0]][c+dxy[(d+2)%8][1]] = math.floor(arr[r+dxy[(d+2)%8][0]][c+dxy[(d+2)%8][1]] + (sand * 0.07))
            arr[r+dxy[(d+6)%8][0]][c+dxy[(d+6)%8][1]] = math.floor(arr[r+dxy[(d+6)%8][0]][c+dxy[(d+6)%8][1]] + (sand * 0.07))
            # 모래 이동 (두칸 양옆 또는 위아래)
            arr[r+2*dxy[(d+2)%8][0]][c+2*dxy[(d+2)%8][1]] = math.floor(arr[r+2*dxy[(d+2)%8][0]][c+2*dxy[(d+2)%8][1]] + (sand * 0.02))
            arr[r+2*dxy[(d+6)%8][0]][c+2*dxy[(d+6)%8][1]] = math.floor(arr[r+2*dxy[(d+6)%8][0]][c+2*dxy[(d+6)%8][1]] + (sand * 0.02))
            # 모래 이동 (대각선 뒤쪽)
            arr[r+dxy[(d+3)%8][0]][c+dxy[(d+3)%8][1]] = math.floor(arr[r+dxy[(d+3)%8][0]][c+dxy[(d+3)%8][1]] + (sand * 0.01))
            arr[r+dxy[(d+5)%8][0]][c+dxy[(d+5)%8][1]] = math.floor(arr[r+dxy[(d+5)%8][0]][c+dxy[(d+5)%8][1]] + (sand * 0.01))
            # 모래 이동 (두칸 앞)
            arr[r+2*dxy[(d)%8][0]][c+2*dxy[(d)%8][1]] = math.floor(arr[r+2*dxy[(d)%8][0]][c+2*dxy[(d)%8][1]] + (sand * 0.05))
            # 모래 이동 (앞 / 남은 것)
            arr[r+dxy[(d)%8][0]][c+dxy[(d)%8][1]] = math.floor(arr[r+dxy[(d)%8][0]][c+dxy[(d)%8][1]] + (sand * 0.55))
            for row in arr:
                temp_sum += sum(row)
            
        tornado += 1

    
