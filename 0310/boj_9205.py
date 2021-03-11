import sys
sys.stdin = open('9205_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 맥주를 파는 편의점 갯수
    n = int(input())
    home = list(map(int, input().split()))