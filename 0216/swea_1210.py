import sys
sys.stdin = open('homework_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):   # 사다리 크기
    N = 10
    ladder = []
    # 사다리 받아오기
    for _ in range(N):
        ladder.append(list(map(int, input().split())))

    # 당첨 지점의 idx 찾기
    for i in range(N):
        if ladder[-1][i] == 2:
            idx = i
    
    # 위 / 왼쪽 / 오른쪽 으로 움직일 수 있는 델타
    dxy = [[0, -1], [-1, 0], [1, 0]]
    # 현재 위치
    row = len(ladder) - 1
    col = idx

    while row > 0:
        # 현재 진행방향 (기본: 위로 시작)
        direction = dxy[0]
        # 위로 한칸 이동
        dx, dy = direction
        row += dy
        col += dx

        # 왼쪽 오른쪽으로 갈수 있는지 체크
        # 갈 수 있다면, 그쪽 방향으로 전환
        if col > 0 and ladder[row][col-1] == 1:
            dx, dy = dxy[1]
        elif col < 9 and ladder[row][col+1] == 1:
            dx, dy = dxy[2]

        # 더이상 왼쪽/오른쪽으로 갈수 없을때까지 왼쪽/오른쪽으로 이동 (왼쪽/오른쪽이 0이거나 벽을 만났을때)
        while ladder[row][col+dx] == 1 and dx != 0:
            row, col = row + dy, col + dx
        
    print("#%d %d" % (tc, col))
