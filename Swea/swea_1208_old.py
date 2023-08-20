import sys
sys.stdin = open('homework.txt', 'r')

T = 10

for t in (1, T+1):
    dump = int(input())
    box_list = list(map(int, input().split()))

    # 카운팅 소트를 위한 리스트
    cnt = [0] * 101
    # 최종 sort된 리스트를 담을 리스트
    sorted_box_list = []

    # count sort 하기
    for box in box_list:
        cnt[box] += 1
    for i in range(101):
        sorted_box_list += [i] * cnt[i]

    print(len(sorted_box_list))
    print(sorted_box_list)
    # dump 횟수만큼 옮기기
    # 만약 min 숫자가 3이고 4번 나왔다
    # sorted_box_list[0] = 3, cnt[3] = 4면
    # 정렬된 리스트에서 마지막 나오는 3의 인덱스는 4-1 인 3
    min_idx = cnt[sorted_box_list[0]] - 1

    # 만약 max 숫자가 100고 2번 나왔다
    # sorted_box_list[99] = 100 cnt[100] = 2
    # 정렬된 리스트에서 제일 처음 나오는 100의 인덱스는 100-2인 98
    max_idx = 100 - cnt[sorted_box_list[99]]

    while dump > 0:
        sorted_box_list[:min_idx] += 1
        sorted_box_list[max_idx:] -= 1
        box_list[min_idx] += 1
        box_list[max_idx] -= 1

        dump -= min_idx + 1


    print(len(sorted_box_list))
