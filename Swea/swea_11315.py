import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def check_omok(omok, N):
    # 가로 체크
    for row in omok:
        streak = 0
        for col in row:
            if col:
                streak += 1
                if streak == 5:
                    return "YES"
            else:
                streak = 0

    # 세로 체크
    for j in range(N):
        streak = 0
        for i in range(N):
            if omok[i][j] == 1:
                streak += 1
                if streak == 5:
                    return "YES"
            else:
                streak = 0

    # 오른쪽 밑으로 내려가는 대각선 체크
    # 시작점 설정
    for i in range(0, N-4):
        streak = 0
        for j in range(0, N-4):
            # 시작점을 기준으로 대각선 다섯개 순회
            for k in range(5):
                if omok[i+k][j+k] == 0:
                    break
            else:
                return "YES"
    
    # 왼쪽 밑으로 내려가는 대각선 체크
    for i in range(0, N-4):
        streak = 0
        for j in range(4, N):
            # 시작점을 기준으로 대각선 다섯개 순회
            for k in range(5):
                if omok[i+k][j-k] == 0:
                    break
            else:
                return "YES"
    return "NO"


for tc in range(1, T+1):
    N = int(input())
    omok = []

    # input값 받기
    for _ in range(N):
        row = list(map(lambda x: 1 if x=='o' else 0, input()))
        omok.append(row)
    
    # 가로 체크
    result = check_omok(omok, N)
    print("#%d %s" % (tc, result))
    
   