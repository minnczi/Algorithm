import sys
sys.stdin = open('Q1_input.txt', 'r')

T = int(input())

# 이동방향 (상하좌우 순서대로)
# 방향 회전시 두칸 뒤에 있는 방향으로 전환된다
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def move(cr, cc, info, inqueue):
    # 기존 미생물 수와 방향 받아오기
    info[2] = 1

    # 원래 있던 칸을 0으로 바꾼다 (원래 있던 칸이 벽이었으면 -1로 바꾼다)
    if inqueue:
        pass
    elif cr == 0 or cr == N-1 or cc == 0 or cc == N-1:
        room[cr][cc] = -1
    else:
        room[cr][cc] = 0
    
    # 새로운 칸으로 이동
    cr, cc = cr+dr[info[1]], cc+dc[info[1]]
    # 케이스 1: 아무것도 없는 칸으로 이동한 경우 --> 그냥 이동한다
    if room[cr][cc] == 0:
        room[cr][cc] = info

    # 케이스 2: 벽 바깥으로 이동한 경우 --> 이동 후 개체 수를 반으로 줄이고 방향을 바꾼다
    elif room[cr][cc] == -1:
        info[0] //= 2
        if info[0] == 0:
            return
        if info[1] % 2:
            info[1] += 1
        else:
            info[1] -= 1
        room[cr][cc] = info

    # 케이스 3-1: 다른 개체가 있는데 그 개체는 아직 이동을 안한 경우 --> 그냥 이동한다, 원래 있던 개체는 queue에 넣는다
    elif room[cr][cc][2] == 0:
        # print('case3')
        global queue
        queue.append([cr, cc, room[cr][cc]])
        if cr == 0 or cr == N-1 or cc == 0 or cc == N-1:
            info[0] //= 2
            if info[0] == 0:
                return
            if info[1] % 2:
                info[1] += 1
            else:
                info[1] -= 1
        room[cr][cc] = info
        
    # 케이스 3-2 다른 개체가 있는데 그 개체도 이미 이동을 한 경우 --> 개체 수를 비교해 방향을 정하고 개체수를 합친다
    else:
        # print('case4')
        original = room[cr][cc]
        # 방향 이동 - 만약 오리지널의 개체수가 더 많았을 경우 temp의 방향을 바꾼다
        if original[0] > info[0]:
            info[1] = original[1]
        
        # 개체수 합치기
        info[0] += original[0]
        room[cr][cc] = info




# N = 셀의 갯수, M = 격리 시간, K = 미생물 군집 갯수 
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    # 벽이 있는 방 만들기
    room = [[-1]*(N)]
    for _ in range(N-2):
        room.append([-1] + [0]*(N-2) + [-1])
    room.append([-1]*(N))

    # 최초 위치 받아오기 --> 0=빈칸, -1=벽, 그외숫자=미생물 수
    # 각 칸에, num, drc, moved(이번 라운드에서 움직였는지 안움직였는지 표시할 변수 - 기본값=0) 를 넣는다 
    for _ in range(K):
        row, col, num, drc = map(int, input().split())
        room[row][col] = [num, drc, 0]

    for i in range(M):
        queue = []
        # 이동하기
        for cr in range(N):
            for cc in range(N):
                info = room[cr][cc]
                if isinstance(info, list) and info[2]==0:
                    move(cr, cc, info, 0)

        for i in queue:
            move(i[0], i[1], i[2], i)

        # 방문 마크 초기화하기
        for cr in range(N):
            for cc in range(N):
                if isinstance(room[cr][cc], list):
                    room[cr][cc][2] = 0
    
    total = 0
    for cr in range(N):
        for cc in range(N):
            if isinstance(room[cr][cc], list):
                total += room[cr][cc][0]
    print("#%d %d" % (tc, total))
            