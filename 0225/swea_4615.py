import sys
sys.stdin = open('4615_input.txt')

T = int(input())

def change_color(row, col, dir, color, opp):
    # 범위 밖으로 벗어났을 경우 재귀 종료
    if board[row][col] == 0:
        return False
    # 상대 돌을 감싸고 있는 내 돌을 발견했을때 트루를 리턴
    elif board[row][col] == color:
        board[row][col] = color
        return True
    # 한칸 이동했을때도 상대방의 돌 색깔이 나온 경우 다음 돌 체크
    result = change_color(row+v[0], col+v[1], dir, color, opp)
    # 만약 내 돌이 상대 돌을 감싸고 있는 형태 였다면, 사이에 있는 상대방 돌을 내 색깔로 변환
    if result:
        board[row][col] = color
    return result

    
# 방향을 나타낼 리스트
delta = {"N":[-1, 0], "E":[0, 1], "S":[1, 0], "W":[0, -1], "NE":[-1, 1], "SE":[1, 1], "SW": [1, -1], "NW": [-1, -1]}
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 인덱스가 1부터 시작하기 때문에, 그리고 인접한 돌 체크할때 인덱스 사용에 편의를 위해서
    # 테두리에 패딩을 넣어준다
    board = [[0] * (N+2) for _ in range(N+2)]
    # 초기 돌 세팅
    board[N//2][N//2], board[N//2+1][N//2+1] = 2, 2
    board[N//2][N//2+1], board[N//2+1][N//2] = 1, 1

    for _ in range(M):
        col, row, color = map(int, input().split())
        # 내 돌을 판위에 올려놓기
        board[row][col] = color
        # 상대방의 돌 색깔
        opp = 1 if color == 2 else 2
        # 8방향으로 영향을 받을 가능성이 있는 상대의 돌이 있는지 체크
        for k, v in list(delta.items()):
            if board[row+v[0]][col+v[1]] == opp:
                change_color(row+v[0], col+v[1], v, color, opp)

    black, white = 0, 0
    for row in board:
        for col in row:
            if col == 1:
                black += 1
            elif col==2:
                white += 1
    print("#%d %d %d" % (tc, black, white))
