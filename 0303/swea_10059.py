result = ['NA', 'MMYY', 'YYMM', 'AMBIGUOUS']

T = int(input())
for tc in range(1, T+1):
    date = input()
    idx = 0
    if 1 <= int(date[0:2]) <= 12:
        idx += 1
    if 1 <= int(date[2:]) <= 12:
        idx += 2
    print("#%d %s" % (tc, result[idx]))