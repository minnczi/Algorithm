
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
answer = 0
def solution(begin, target, words):

    dfs(begin, target, 0, words)
    return answer

def change(fr, to):
    for i in range(len(fr)):
        if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]:
            return True
    return False

def dfs(begin, target, d, words):
    global answer
    # print(begin)
    # print(words)
    if begin == target:
        # print(d)
        answer = d
        return
    else:
        if len(words) == 0:
            return 
        for w in range(len(words)):
            if change(begin, words[w]):
                word = words[:w]+words[w+1:]
                dfs(words[w], target, d+1, word)