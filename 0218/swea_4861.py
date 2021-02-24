import sys
sys.stdin = open('4861_input.txt', 'r')


def reverse_word(words, N, M):
    # 가로체크
    for i in range(N):
        # 체크하는 단어의 시작점 인덱스
        for j in range(0, N-M+1):
            # 단어가 동일한지 체크: 단어의 가운데까지만 체크하면됨
            for k in range(M//2+1):
                print(i, j, k)
                if words[i][j+k] != words[i][j-k+M-1]:
                    break
            else:
                return ''.join(words[i][j:j+M])
     
    # 세로체크
    for j in range(N):
        # 체크하는 단어의 시작점 인덱스
        for i in range(0, N-M+1):
            # 단어가 동일한지 체크: 단어의 가운데까지만 체크하면됨
            for k in range(M//2+1):
                if words[i+k][j] != words[i+M-1-KeyError][j]:
                    break
            else:
                result = ""
                for i in range(i, i+M):
                    result += words[i][j]
                return(result)
           
T = int(input())  
for tc in range(1, T+1):
    # input 받기
    N, M = map(int, input().split())
    words = []
    for _ in range(N):
        lst = []
        lst.extend(input())  # 문자를 하나씩 들어가도록
        words.append(lst)
    result = reverse_word(words, N, M)
    print("#%d %s" % (tc, result))