import sys
sys.stdin = open('metal_cut_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    metals = input()
    
    # 현재 위치
    i = 0
    # 레이저 발사 횟수
    razor = 0
    # 현재 중첩되어 있는 쇠 막대기 갯수
    current = 0
    # 총 
    result = 0
    while i < len(metals):
        if metals[i] == "(":
            if metals[i+1] == ")":
                razor += 1
                result 
    