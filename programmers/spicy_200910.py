import heapq as hq

def solution(scoville, K):
    answer =0
    hq.heapify(scoville)
    
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        mix = first + second * 2
        hq.heappush(scoville, mix)
        answer += 1
    return answer

# def solution(scoville, K):
#     answer = 0
#     # scoville 지수가 K 보다 낮은 수의 집합
#     non_spicy = [s for s in scoville if s < K]
    
#     # 모든 수가 K보다 높을경우 바로 answer 반환
#     if len(non_spicy) == 0:
#         return answer
    
#     # K보다 매운 음식이 하나라도 있으면 True 아니면 False
#     if scoville ==  non_spicy:
#         spicy_exists = False
#     else:
#         spicy_exists = True
    
#     #만약 K 보다 낮은 음식 2개가 있어서 섞을수 있다면 2개를 섞음
#     while len(non_spicy) > 1:
#         non_spicy.sort()
#         mixed = non_spicy.pop(0) + non_spicy.pop(1) * 2
#         # 만약 섞은 결과도 K 보다 작다면 non_spicy에 다시 append
#         if mixed < K:
#             non_spicy.append(K)
#         answer += 1
        
#     if spicy_exists:
#         answer += 1
#     else:
#         answer = -1
#     return answer