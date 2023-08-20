import sys
sys.stdin = open('11579_input.txt', 'r')

T = int(input())

def check_dup(word, start):
    for i in range(start, len(word)-1):
        if word[i] == word[i+1]:
            word.pop(i)
            word.pop(i)
            start = 0 if i == 0 else i-1
            return check_dup(word, start)
    return len(word)

for tc in range(1, T+1):
    word = []
    word.extend(input())
    print("#%d %d" % (tc, check_dup(word, 0)))
