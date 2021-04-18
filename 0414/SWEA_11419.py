# 11419. Baby-Gin Game
def baby_gin():
    gin_count = 0
    # triplet 체크하기
    i = 0
    while i < 10:
        if card_counts[i] >= 3:
            card_counts[i] -= 3
            gin_count += 1
            continue
        i += 1
    # run 체크하기    
    i = 0
    while i <= 7:
        if (card_counts[i] and card_counts[i+1] and card_counts[i+2]) >= 1:
            card_counts[i] -= 1
            card_counts[i+1] -= 1
            card_counts[i+2] -= 1
            gin_count += 1
            continue
        i += 1
    return 'Baby Gin' if gin_count == 2 else 'Lose'

T = int(input())
for tc in range(1, T+1):
    card_counts = [0] * 10
    num = input()
    for i in range(len(num)):
        card_counts[int(num[i])] += 1
    result = baby_gin()
    print("#%d %s" % (tc, result))