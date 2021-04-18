import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # N = 컨테이너 수, M = 트럭 수
    N, M = map(int, input().split())
    # containers = 화물 배열, trucks = 트럭 배열
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    # 총 화물 적재 용량
    total = 0
    # 화물과 트럭을 내림차순 정렬하고
    # 트럭의 적재용량보다 가벼운 화물이 나오는 순간 트럭에 싣고 break
    for i in range(M):
        for j in range(N):
            if containers[j] <= trucks[i]:
                total += containers[j]
                containers.pop(j)
                N -= 1
                break
    print("#%d %d" % (tc, total))