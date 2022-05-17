N = int(input())

# [number, color, weight, total] 정보를 저장
# total = 해당 공이 먹을 수 있는 공의 합 (정답이 저장될 부분)
balls = [[i] + list(map(int, input().split())) + [0] for i in range(N)]
sorted_balls = sorted(balls, key=lambda x: x[2])

# 색깔별 무게 합
colors = [0] * (N+1)

pw = 0 # previous weight
sw = 0 # sum weight

# 동일한 무게의 공들이 나왔을 때, 임시적으로 담아두기 위한 stack
stack = []
for i in range(len(balls)):
    # number, color, weight, total
    n, c, w, t = sorted_balls[i]
    # 이전 공과 색깔이 다르다면
    if w != pw:
        tsw = 0
        while stack:
            tc, tw = stack.pop()
            colors[tc] += tw
            tsw += tw
        sw += tsw

    stack.append([c, w])
    balls[n][3] = sw - colors[c]
    pw = w

for i in range(N):
    print(balls[i][3])