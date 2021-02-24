import sys
sys.stdin = open('palindrome_input.txt', 'r')


# 길이 N의 palindrome이 존재하는지 체크하는 함수
# N은 palindrome의 길이
def check_palindrome(words, N):
    for lst in words:
        for i in range(0, 100-N+1):
            for j in range(0, N//2):
                # print(lst[i+j], lst[N-1-j+i])
                if lst[i+j] != lst[N-1+i-j]:
                    break
            else:
                # print(i, j)
                return True
    return False
    
           
T = 10
for tc in range(1, T+1):
    # input 받기
    tc = int(input())
    words_garo = []
    words_sero = []

    # 가로 / 세로로 방향으로 묶은 2D 리스트 생성
    for _ in range(100):
        lst = []
        lst.extend(input())  # 문자를 하나씩 들어가도록
        words_garo.append(lst)
    words_sero = list(map(list, zip(*words_garo)))

    for N in range(100, 0, -1):
        if check_palindrome(words_garo, N) or check_palindrome(words_sero, N):
            result = N
            break
    
    print("#%d %d" % (tc, result))
