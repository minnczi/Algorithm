import sys
sys.stdin = open('11606_input.txt', 'r')

T = int(input())

# 델타 (상하좌우 순으로)
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 2 --> 3을 찾던 3 --> 2를 찾던 상관없기 때문에 위에서 부터 탐색하기 위해 3 --> 2로 가는 경로 탐색
# ans의 값은 갈 수 없는 길을 찾았을때 0, 갈 수 있는 길을 찾았을때 1
def find_path(maze, r, c):
    # 현재 노드에 방문 표시
    visited[r][c] = 1
    # 만약 벽이라면 0을 리턴하고 종료
    if maze[r][c] == 1:
        return 0
    # 도착 지점을 찾았다면 1을 리턴하고 종료
    elif maze[r][c] == 3:
        return 1
    # 만약 열려 있는 길에 도착했다면, 그 길을 중심으로 주변 탐색
    else:
        for dr, dc in drc:
            # 현재 위치 기준으로 상하좌우중 탐색하지 않은 노드가 있다면, 재귀 함수를 호출하여 다음 노드 탐색
            if not visited[r+dr][c+dc]:
                ans = find_path(maze, r+dr, c+dc)
                # 탐색 도중이라도, 갈 수 있는 길을 하나라도 찾았다면, 더이상 탐색할 필요가 없으므로 ans == 1일때는 for loop 탈출            
                if ans:
                    return ans
    return 0


for tc in range(1, T+1):
    N = int(input())
    
    # maze 입력 받기 + 시작 좌표 찾기
    maze = [[1] * (N+2)]
    for i in range(1, N+1):
        temp = [1] + list(map(int, input())) + [1]
        for j in range(N+2):
            if temp[j] == 2:
                sr, sc = i, j
        maze.append(temp)
    maze += [[1] * (N+2)]

    # 방문한 노드를 표시할 matrix 만들기
    visited = [[0]*(N+2) for _ in range(N+2)]

    res = find_path(maze, sr, sc)
    print("#%d %d" % (tc, res))