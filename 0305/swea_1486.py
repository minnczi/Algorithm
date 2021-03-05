import sys
sys.stdin = open('1486_input.txt', 'r')

T = int(input())

def find_min(N, B, heights):
    min_height = 1000000
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            if i & (1 << j):
                temp += heights[j]
        if B <= temp < min_height:
            min_height = temp
    return min_height - B


for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    print("#%d %d" % (tc, find_min(N, B, heights)))