def find_food_idx(food_times, k):
    N = len(food_times) # 전체 음식 갯수
    idx = 0 # 현재 앞에 있는 음식의 인덱스
    for i in range(k):
        # 1. 만약 음식이 없다면 있을때까지 찾기
        if not food_times[idx]:
            cnt = 0 # 음식을 몇개 검사했는지 체크하는 카운트
            # 2. 만약 한바퀴를 다 돌았는데도 음식이 없다면 끝내기
            while not food_times[idx]:
                if cnt >= N:
                    return -1
                idx = (idx + 1) % N
                cnt += 1
        # 3. 음식 먹기
        food_times[idx] -= 1
        idx = (idx + 1) % N
    return idx + 1
    
    
def solution(food_times, k):
    answer = find_food_idx(food_times, k)
    return answer