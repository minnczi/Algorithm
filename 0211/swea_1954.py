# 풀이 1 단순 인덱스 접근으로 풀기
T = int(input())

for t in range(1, T+1):
    N = int(input())
    start = 0
    end = N-1
    snail = [[0]*N for _ in range(N)]
    num = 1

    # 달팽이가 작아지다가 가운데에서 만나기전까지 반복
    while end >= (N//2):
        if start == end:
            snail[start][end] = str(num)
            break

        # 윗줄 쓰기
        for j in range(start, end):
            snail[start][j] = str(num)
            num += 1

        # 오른쪽 쓰기
        for i in range(start, end):
            snail[i][end] = str(num)
            num += 1

        # 아랫줄 쓰기
        for j in range(end, start, -1):
            snail[end][j] = str(num)
            num += 1

        # 왼쪽 쓰기
        for i in range(end, start, -1):
            snail[i][start] = str(num)
            num += 1

        start += 1
        end -= 1

    print("#%d" % (t))
    for row in snail:
        print(" ".join(row))

# 풀이 2 델타 사용해서 풀기 (현재 인덱스 기준으로 얼마나 이동해야되는지 계산)
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # 우하좌상 순으로 (실제 달팽이가 채워지는 순서)
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    move = N-1

    # 현재 위치
    i = j = -1
    num = 1

    while move > 0:
        # 코드가 실행되면 테두리 한바퀴를 돌고 제자리로 돌아오기 때문에 안쪽 레이어를 채우려면 i, j를 1씩 증가
        i += 1
        j += 1
        # dx, dy 방향으로
        for dx, dy in dxy:
            # move칸만큼 이동하며 번호 찍기
            for _ in range(move):
                snail[i][j] = num
                i += dx
                j += dy
                num += 1
        move -= 2

    # 홀수칸이면 마지막 가운데 한칸이 비므로 채워줘야함
    if move == 0:
        snail[i+1][j+1] = num

    print("#%d" % (tc))
    for row in snail:
        print(*row)