# Baby Gin Game
import sys
sys.stdin = open('input.txt', 'r')

# 카드를 한장 더 추가로 받았을때, run, triplet, single 조합이 생기는지 체크하는 함수
def add_card(player, num):
    for r in runs[player]:
        if num == (r[0]-1 or r[1]+1):
            return 1
    for t in triplets[player]:
        if num == t:
            return 1
    for s in single[player]:
        if num == s-1:
            runs[player].append([num, s])
        elif num == s+1:
            runs[player].append([s, num])
        elif num == s:
            triplets[player].add(num)
    single.add(num)
    return 0


def find_winner(player1, player2):
    if player1 & player2:
        return 0
    elif player1:
        return 1
    return 2


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    runs = [[], []]
    triplets = [set(), set()]
    single = [{cards[0]}, {cards[1]}]
    winner = 0
    for i in range(2, len(cards), 2):
        player1 = add_card(0, cards[i])
        player2 = add_card(1, cards[i+1])
        if player1 or player2:
            winner = find_winner(player1, player2)
            break
    print("#%d %d" % (tc, winner))
