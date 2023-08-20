import sys
sys.stdin = open('9778_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    deck = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

    N = int(input())
    hand = 0
    for _ in range(N):
        card = int(input())
        hand += card
        deck[card] -= 1

    if hand <= 10:
        result = 'GAZUA'
    elif sum(deck[21-hand+1:]) < sum(deck[2:21-hand+1]):
        result = "GAZUA"
    else:
        result = "STOP"
        
    print("#%d %s" % (tc, result))
