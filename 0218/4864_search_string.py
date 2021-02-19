import sys
sys.stdin = open('string_input.txt', 'r')

T = int(input())

def search_string(str1, str2):
    # i가 key의 인덱스, j가 원본 스트링의 인덱스
    i, j, N, M = 0, 0, len(str1), len(str2)
    while i < N and j < M:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
        if i == N:
            return 1
    return 0

for tc in range(1, T+1):
    str1, str2, = input(), input()
    result = search_string(str1, str2)
    print("#%d %d" % (tc, result))
    