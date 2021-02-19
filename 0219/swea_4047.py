import sys
sys.stdin = open('4047_input.txt', 'r')

T = int(input())

# 카드를 출력할 순서
order = ['S', 'D', 'H', 'C']
# 이렇게 했더니 하나의 value를 업뎃했을때 모든 value가 바꼈다... 왜그러지...
# count_dict = dict.fromkeys(order, [])
def count_cards():
    count_dict = {'S': [], 'D': [], 'H': [], 'C': []}
    cards = input()

    for i in range(0, len(cards), 3):
        k = cards[i]
        v = cards[i+1:i+3]
        # 만약 넣으려 하는 v값이 이미 list에 있다면, 에러
        if v in count_dict[k]:
            return "ERROR"
        # 아니라면 key에 해당하는 리스트에 추가
        else:
            count_dict[k].append(v)

    result = []
    for card in order:
        result.append(str(13-len(count_dict[card])))
    return " ".join(result)

# 출력
for tc in range(1, T+1):
    print('#%d %s' % (tc, count_cards()))

        