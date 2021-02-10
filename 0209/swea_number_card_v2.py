import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    cards = str(input())

    card_count = [0] * 10

    for i in cards:
        card_count[int(i)] += 1

    max_card = 9
    for i in range(8, -1, -1):
        if card_count[i] > card_count[max_card]:
            max_card = i

    print("#%d %d %d" % (t, max_card, card_count[max_card]))
