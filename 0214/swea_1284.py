T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    # A사 요금
    cost_a = P * W

    # B사 요금
    cost_b = Q if W <= R else Q + (W-R)*S

    # 비교
    cost = cost_a if cost_a < cost_b else cost_b
    # 출력
    print("#%d %d" % (tc, cost))