import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    cards = str(input())

    # 카드와 그 카드의 갯수가 담겨있는 dict, 일단 첫번째 카드만 넣어놓기
    all_dict = {cards[0]: 1}
    # 가장 많은 카드와 카드의 갯수를 각각 변수로 저장
    max_card = cards[0]
    max_cnt = 1

    # 카드 리스트를 돌면서 카드 갯수를 세고, 카드 갯수가 현재 max보다 클 경우 max_card와 max_cnt를 업데이
    for card in cards[1:]:
        # 현재까지 어떤 카드가 몇번 나왔는지 찾아야되는데, 만약 없으면 아직 한번도 안나온 카드이므로 0
        all_dict[card] = all_dict.get(card, 0) + 1
        cnt = all_dict[card]

        if cnt > max_cnt:
            max_card = card
            max_cnt = cnt

        elif cnt == max_cnt and card > max_card:
            max_card = card
            max_cnt = cnt

    print("#%d %s %d" % (t, max_card, max_cnt))

