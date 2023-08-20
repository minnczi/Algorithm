import sys
sys.stdin = open('9940_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    if sorted(arr) == list(range(1, N+1)):
        result = "Yes"
    else:
        result = "No"
    print("#%d %s" % (tc, result))