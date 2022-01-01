import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # input 받기
    n, k = map(int, input().split())

    puzzle = []
    for _ in range(n):
        lst = list(map(int, input().split()))
        lst.append(0)
        puzzle.append(lst)
    
    puzzle.append([0]*(n+1))
    print(puzzle)
    
    answer = 0
    streak = 0 # 1이 연속적으로 나온 횟수
    # 가로 먼저 체크
    for row in puzzle:
        for i in row:
            if i:
                streak += 1
            else:
                # 이전까지 쌓인 연속 횟수가 k번 이었다면
                if streak == k: 
                    answer += 1
                    streak = 0
                else:
                    streak = 0
    # 세로 체크
    for j in range(n):
        for i in range(n):
            if puzzle[i][j]:
                streak += 1
            else:
                if streak == k:
                    answer += 1
                else:
                    streak = 0
    print(f'#{test_case} {answer}')