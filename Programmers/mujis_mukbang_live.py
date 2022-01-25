from heapq import heappush, heappop

def solution(food_times, k):
    answer = -1
    h = []
    
    # 1. 남은 시간 기준으로 정렬
    for i in range(len(food_times)):
        # 배열을 heappush할 경우, 맨 앞 원소 기준으로 자동 정렬됨
        heappush(h, [food_times[i], i+1])
    
    N = len(food_times)
    previous = 0
    
    # 2. 가장 빨리 없어지는 음식부터 하나씩 찾으면서 시작
    while h:
        # 3. 음식 하나가 없어지는데 걸리는 시간 = 남은 음식 * 회전수
        t = N * (h[0][0]-previous)
        # 3-1
        if k >= t:
            k -= t
            previous, _ = heappop(h)
            N -= 1
        # 3-2
        else:
            # 남은 음식을 번호순으로 정렬한다
            h.sort(key=lambda x: x[1])
            answer = h[k % len(h)][1]
            break
    return answer