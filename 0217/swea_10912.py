import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for tc in range(1, T+1):
    word = input()
    word_count = [0] * 26
    result = ""

    for i in range(len(alpha)):
        word_count[i] = word.count(alpha[i])
    
    for i in range(len(alpha)):
        if word_count[i] % 2:
            result += alpha[i]
    
    if result == "":
        result = "Good"
    
    print("#%d %s" % (tc, result))