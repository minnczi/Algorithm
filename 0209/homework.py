import sys
sys.stdin = open('homework.txt', 'r')

T = 10

for t in range(1, T+1):
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

    for n in range(dump):
        cur_min = sorted_box_list[0]
        cur_max = sorted_box_list[99]

        if cur_max - cur_min == 1:
            break

        sorted_box_list[0] = cur_min = cur_min + 1
        sorted_box_list[99] = cur_max = cur_max - 1

        # 새로운 min / max 찾아서 자리 바꾸기
        if cur_min > sorted_box_list[1]:
            for i in range(1, 100):
                if sorted_box_list[i] >= cur_min:
                    sorted_box_list[0], sorted_box_list[i-1] = sorted_box_list[i-1], sorted_box_list[0]
                    break

        if cur_max < sorted_box_list[98]:
            for i in range(98, 0, -1):
                if sorted_box_list[i] <= cur_max:
                    sorted_box_list[99], sorted_box_list[i+1] = sorted_box_list[i+1], sorted_box_list[99]
                    break

    print("#%d %d" % (t, sorted_box_list[99] - sorted_box_list[0]))



