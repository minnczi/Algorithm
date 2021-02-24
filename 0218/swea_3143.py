import sys
sys.stdin = open('3143_input.txt', 'r')

T = int(input())

# for tc in range(1, T+1):
#     A, B = input().split()
#     len_A, len_B = len(A), len(B)

#     shortcut = 0
#     for i in range(len_A-len_B+1):
#         for j in range(len_B):
#             if A[i+j] != B[j]:
#                 break
#         else:
#             shortcut += 1
#     # 단축키를 한번 쓸때마다 키 누르는 횟수가 len_B - 1 만큼 감소
#     result = len_A - shortcut*(len_B-1)
#     print("#%d %d" % (tc, result))

for tc in range(1, T+1):
    A, B = input().split()
    len_A, len_B = len(A), len(B)

    result = len_A - (len_B-1) * A.count(B)
    print("#%d %d" % (tc, result))

    