import sys
sys.stdin = open('4880_input.txt', 'r')

T = int(input())

# rps[winner][player] --> 현재 우승자가 winner이고 도전자가 player일때
# 도전자 입장에서의 경기결과 (d: 무승부, w: 도전자 승리, l: 도전자 패배)
# ex) rps[1][2] = 'w' = 우승자가 가위, 도전자가 바위이므로, 도전자의 승리 
rps_lst = [0, [0, 'd', 'w', 'l'], [0, 'l', 'd', 'w'], [0, 'w', 'l', 'd']]

def rps(player):
    global winner
    # 이전의 위너가 없는 상황
    if winner == -1:
        winner = player
    else:
        result = rps_lst[arr[winner]][arr[player]]
        if result == 'w':
            winner = player
        elif result == 'd':
            winner = min(winner, player)
    return

def tournament(arr, s, e):
    # 그룹 나누기
    # 그룹에 혼자 남았을때 승부
    if s == e:
        # 승자 판별하기
        player = s
        rps(player)
    else:
        mid = (s+e) // 2
        tournament(arr, s, mid)
        tournament(arr, mid+1, e)
    return winner


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    winner = -1
    winner = tournament(arr, 0, len(arr)-1) + 1 
    print("#%d %d" % (tc, winner))