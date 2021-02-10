import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    grade_map = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    grade = []
    # cutoff = [] # 커트라인을 담을 리스트

    for _ in range(n):
        # a = 중간, b = 기말, c = 과제
        a, b, c = map(int, input().split())
        grade.append(a*0.35 + b*0.45 + c*0.2)
    
    # 내림차순 정렬된 성적
    grade_s = sorted(grade, reverse=True)
    print(grade_s)
    
    map_idx = 0
    for i in range(int(len(grade_s)/10-1), len(grade_s), int(len(grade_s)/10)):
        print(i, grade_s[i])
        if grade[k] >= grade_s[i]:
            print(f'#{test_case} {grade_map[map_idx]}')
            break
        map_idx += 1
    
