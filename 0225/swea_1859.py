import sys
sys.stdin = open('1859_input.txt', 'r')

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     prices = list(map(int, input().split()))
#     max_idx = prices.index(max(prices))
    
#     result = 0
#     while max_idx != 0:
#         # max_idx 전까지 사기
#         cost = sum(prices[0:max_idx])
#         # max_idx에서 팔기
#         result += (prices[max_idx] * max_idx) - cost

#         # max_idx+1 부터 끝까지 남은 가격들로 새로운 리스트 만들기
#         prices = prices[max_idx+1:]
#         if not prices:
#             break
#         # 새로운 max_idx 구하기
#         max_idx = prices.index(max(prices))
        
#     print("#%d %d" % (tc, result))

for tc in range(1, T + 1):
    length = int(input())
    prices = list(map(int, input().split()))
    max_price = prices[-1]
    answer = 0

    for idx in range(len(prices)-2, -1, -1):
        if max_price >= prices[idx]:
            answer += max_price - prices[idx]
        else:
            max_price = prices[idx]
    print('#{} {}'.format(tc, answer))