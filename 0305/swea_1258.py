import sys
sys.stdin = open('1258_input.txt', 'r')

T = int(input())

def sorter(square):
    area = square[0] * square[1]
    row = square[0]
    return(area, row)


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    squares = []

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            # 사각형 시작 지점 발견!
            if arr[i][j]:
                row = col = 0
                temp_i, temp_j = i, j
                # 행 갯수 체크
                while arr[temp_i][j] and temp_i < N:
                    row += 1
                    temp_i += 1
                # 열 갯수 체크
                while arr[i][temp_j] and temp_j < N:
                    col += 1
                    temp_j += 1
                # 사각형 추가
                squares.append((row, col))
                
                # 사각형 넓이 안에 방문 체크
                for k in range(i, i+row):
                    for l in range(j, j+col):
                        visited[k][l] = 1
    
    num = len(squares)
    # 정렬
    squares = sorted(squares, key=sorter)
    # nested list를 list로 바꾸기
    result = [str(i) for square in squares for i in square]
    print("#%d %d %s" % (tc, num, " ".join(result)))

    