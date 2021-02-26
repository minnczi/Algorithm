import sys
sys.stdin = open('1860_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 사람들 입장 시간
    ppl = list(map(int, input().split()))
    # 제일 늦게 들어오는 사람
    last = max(ppl)

    # 시간대별로 몇명의 사람이 들어오는지 담을 배열
    ppl_arr = [0] * (last+1)
    for i in ppl:
        ppl_arr[i] += 1

    cnt = 0
    sec = 0