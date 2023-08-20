import sys
sys.stdin = open('16935.txt', 'r')

# 상하반전
def upside_down(lst, N, M):
    new_list = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            new_list[i][j] = lst[N-1-i][j]
    return new_list

# 좌우반전
def flip_sides(lst, N, M):
    new_list = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            new_list[i][j] = lst[i][M-1-j]
    return new_list

# 오른쪽으로 90도회전
def reverse_map(lst):
    return list(reversed(lst))

def rotate_90_right(lst, n, m):
    global N, M
    N, M = m, n
    return list(map(reverse_map, list(zip(*lst))))

# 왼쪽으로 90도회전
def rotate_90_left(lst, n, m):
    global N, M
    N, M = m, n
    return list(map(list, reversed(list(zip(*lst)))))

def rotate_sections_90_right(lst, N, M):
    new_list = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if (i < N/2) and (j < M/2):
                new_list[i][j+(M//2)] = lst[i][j]
            elif (i < N/2) and (j >= M/2):
                new_list[i+(N//2)][j] = lst[i][j]
            elif (i >= N/2) and (j >= M/2):
                new_list[i][j-(M//2)] = lst[i][j]
            else:
                new_list[i-(N//2)][j] = lst[i][j]

    return new_list
        

def rotate_sections_90_left(lst, N, M):
    new_list = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if (i < N/2) and (j < M/2):
                new_list[i+(N//2)][j] = lst[i][j]
            elif (i < N/2) and (j >= M/2):
                new_list[i][j-(M//2)] = lst[i][j]
            elif (i >= N/2) and (j >= M/2):
                new_list[i-(N//2)][j] = lst[i][j]
            else:
                new_list[i][j+(M//2)] = lst[i][j]
                
    return new_list


# 여기서 부터 실행 시작
N, M, R = map(int, input().split())

# 리스트 인풋 받기
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

# 해야 할 작업 리스트
tasks = list(map(int, input().split()))

# 작업 호출 및 수행
for task in tasks:
    if task == 1:
        lst = upside_down(lst, N, M)
    elif task == 2:
        lst = flip_sides(lst, N, M)
    elif task == 3:
        lst = rotate_90_right(lst, N, M)
    elif task == 4:
        lst = rotate_90_left(lst, N, M)
    elif task == 5:
        lst = rotate_sections_90_right(lst, N, M)
    else:
        lst = rotate_sections_90_left(lst, N, M)

for row in lst:
    print(" ".join(list(map(str, row))))