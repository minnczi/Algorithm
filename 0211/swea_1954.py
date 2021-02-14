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