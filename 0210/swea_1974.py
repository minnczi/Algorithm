import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
def issudoku(S):
    # row 검증
    for row in S:
        if len(row) != len(set(row)):
            return 0
    
    # column 검증
    for col in zip(*S):
        if len(col) != len(set(col)):
            return 0
    
    # square 검증 --> 가로 방향으로 이동하면서 square 하나씩 탐색
    for i in range(0, 7, 3):
        for j in range(0, 7, 3): 
            square = S[i][j:j+3] + S[i+1][j:j+3] + S[i+2][j:j+3]
            if len(square) != len(set(square)):
                return 0
    return 1

for t in range(1, T+1):
    # 입력 받는 부분
    S = []
    for _ in range(9):
        row = list(map(int, input().split()))
        S.append(row)
    # issudoku 함수 호출
    result = issudoku(S)
    print("#%d %d" % (t, result))