import sys
sys.stdin = open('test_input.txt', 'r')

# for문으로 구현
# for _ in range(10):
#     tc = int(input())
#     key, string = input(), input()
    
#     ans = 0
#     for i in range(len(string)-len(key)+1):
#         for j in range(len(key)):
#             if key[j] != string[i+j]:
#                 break
#         else:
#             ans += 1
    
#     print("#%d %d" % (tc, ans))


# while문으로 구현
for _ in range(10):
    tc = int(input())
    key, string = input(), input()
    K, S = len(key), len(string)

    # i = str 인덱스    j = key 인덱스
    i = j = 0
    ans = 0
    while i < S and j < K:
        if string[i] != key[j]:
            i = i - j
            j = -1
        # 같다면 그냥 proceed
        i = i + 1
        j = j + 1
        # 찾았을때
        if j == K:
            ans += 1
            i = i - j + 1
            j = -1
    
    print("#%d %d" % (tc, ans))

