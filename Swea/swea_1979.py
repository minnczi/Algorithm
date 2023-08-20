import sys
sys.stdin = open('1979_input.txt', 'r')

T = int(input())

def check_place(puzzle):
    answer = 0

    streak = 0 # 1이 연속적으로 나온 횟수
    # 가로 체크
    for row in puzzle:
        for i in row:
            if i:
                streak += 1
            else: # 벽을 만났을때
                # 이전까지 쌓인 연속 횟수가 k번 이었다면
                if streak == k: 
                    answer += 1
                streak = 0
    # 세로 체크
    for j in range(len(puzzle)):
        for i in range(len(puzzle)):
            if puzzle[i][j]:
                streak += 1
            else:
                if streak == k:
                    answer += 1
                    streak = 0
                else:
                    streak = 0
    return answer

for test_case in range(1, T + 1):
    # input 받기
    n, k = map(int, input().split())

    # 퍼즐 초기화
    puzzle = []
    # 한줄 + 0 받아오기
    for _ in range(n):
        lst = list(map(int, input().split()))
        lst.append(0)
        puzzle.append(lst)
    
    # 퍼즐 맨 마지막줄에 0으로 된 한줄 받아오기 (벽 만들기)
    puzzle.append([0]*(n+1))
    
    # 함수 호출
    answer = check_place(puzzle)
    print(f'#{test_case} {answer}')