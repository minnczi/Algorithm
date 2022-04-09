# 집의 갯수, 공유기의 갯수
N, C = map(int, input().split())

# 집 위치 배열
houses = sorted([int(input()) for _ in range(N)])
# 집과 집 사이의 거리 배열
dist = [houses[i+1] - houses[i] for i in range(N-1)]
# 공유기와 공유기 사이에 나올 수 있는 최대 거리
max_dist = -1

# 공유기 간의 거리가 x라고 가정했을 때, 공유기를 C보다 많게 / 적게 설치 가능한지 판별하는 함수
# C개보다 적게 설치 가능하다 (less) -> 거리를 줄여야 된다
# C개보다 많이 설치 가능하다 (more) -> 거리를 늘려도 된다
# 정확히 C개 설치 가능하다 (equal) -> 거리를 늘려도 된다
def wifi_lm(x):
    global max_dist
    cnt = 1 # 시작 지점에 하나 설치하고 시작
    temp_dist = 0
    for d in dist:
        temp_dist += d
        if temp_dist >= x:
            cnt += 1
            if cnt == C:
                break
            temp_dist = 0
    if cnt < C:
        return "less"
    else:
        max_dist = x
        return "more"
    
left, right = 0, houses[-1]
while left <= right:
    mid = (left + right + 1) // 2
    if wifi_lm(mid) == "less":
        right = mid - 1
    else:
        left = mid + 1

print(max_dist)
