import sys
sys.stdin = open('sample_input_color.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 사각형의 총 갯수
    N = int(input())
    # 칠해진 영역을 담을 리스트
    result = [[0] * 10 for _ in range(10)]

    # 첫번째 사각형 칠하기
    r1, c1, r2, c2, prev_color = map(int, input().split())
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            result[i][j] = prev_color
    
    # 그 다음 사각형 부터 비교하면서 공통적으로 1이나오면 칠하기
    for m in range(N-1):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if result[i][j] == 0:
                    result[i][j] = color
                elif result[i][j] != color:
                    result[i][j] = 3

    total = 0
    for i in result:
        for j in i:
            if j == 3:
                total += 1
    
    print("#%d %d" % (tc, total))
