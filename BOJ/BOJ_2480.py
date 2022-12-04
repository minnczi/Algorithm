dice = sorted(list(map(int, input().split())))

# 같은 눈이 3개인 경우
if dice[0] == dice[1] == dice[2]:
    print(10000 + dice[0] * 1000)

# 모두 다른 눈인 경우
elif dice[0] != dice[1] != dice[2]:
    print(dice[2] * 100)

# 2개만 같은 눈인 경우
else:
    print(1000 + dice[1] * 100)
