import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

mirror_alpha = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
for tc in range(1, T+1):
    word = input()

    result = ""
    for i in range(len(word)-1, -1, -1):
        result += mirror_alpha.get(word[i])
    
    print("#%d %s" % (tc, result))