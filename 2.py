import sys

sys.stdin = open('input.txt')

# input 받기
N, M, K = map(int, input().split())

board = []
dist_1 = []
dist_2 = []

for _ in range(N):
    row = list()
    row.extend(input())
    board.append(row)


# 시작하는 가운데 지점을 선별하는 코드
mid_x, mid_y = (K-1)//2, (K-1)//2
max_x, max_y = (N-(K-1)//2)-1, (M-(K-1)//2-1)


def init_sum_dist(board, x, y):
    mid_x, mid_y = x+(K-1)//2, y+(K-1)//2
    sum1, sum2 = 0, 0
    dist_1 = [[0]*K for _ in range(K)]
    dist_2 = [[0]*K for _ in range(K)]

    for i in range(x, x+K):
        for j in range(y, y+K):
            player = board[i][j]
            if player == ".":
                continue

            dist = abs(mid_x-i) + abs(mid_y-j)
            if player == '1':
                dist_1[i-x][j-y] = dist
            else:
                dist_2[i-x][j-y] = dist

    print(dist_1, dist_2)
    # print(sum(dist_1), sum(dist_2))
    return sum1, sum2


# def update_sum_list(board, x, y, sum_1, sum_2):
#     mid_x, mid_y = x+(K-1)//2, y+(K-1)//2
#     for j in range(y, y+K):
#         if board[x-1][j] == "1":
#             sum_1 -= 1

#         if board[x+k][j] == "1":


min_sum = 1000000000
# 시작하는 지점
for x in range(N-K+1):
    for y in range(M-K+1):
        sum1, sum2 = init_sum_dist(board, x, y)

print(min_sum)
