answer = []


def solution(prices, idx):
    if len(prices)


def solution(prices):
    answer = []
    for i in range(len(prices)):
        moment_price = prices[i]
        remaining_prices = prices[i + 1:]
        seconds = 0

        # price 리스트의 마지막 아이템일때 break
        if len(remaining_prices) == 1:
            answer.append(1)
            answer.append(0)
            break

        for price in remaining_prices:
            seconds += 1
            if price < moment_price:
                break
            else:
                continue
        answer.append(seconds)
    return answer

# answer = []
# def solution(prices):
#     if len(prices) == 2:
#         answer.append(1)
#         answer.append(0)
#         return answer
#     else:
#         seconds = 0
#         for i in range (1,len(prices)):
#             if prices[i] >= prices[0]:
#                 seconds += 1
#             else:
#                 answer.append(seconds+1)
#                 return solution(prices[1:])
#         answer.append(seconds)
#         return solution(prices[1:])

