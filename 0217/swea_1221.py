import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())

# 새로운 숫자들을 정렬될 순서대로 담아놓은 리스트
GNS = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(T):
    tc, N = input().split()
    arr = input().split()

    # 카운팅 정렬에서 카운트를 담을 배열
    gns_count = [0] * len(GNS)
    
    # arr을 돌면서 nums[i]와 같은 값이 나올때마다 nums_count[i]가 1씩 증가
    for i in range(len(arr)):
        for j in range(len(GNS)):
            if arr[i] == GNS[j]:
                gns_count[j] += 1
                break
    
    # 정렬된 숫자들을 담을 리스트
    sorted_nums = []
    # nums[i]가 등장한 횟수 (nums_count에 저장되어있는 횟수) 만큼 최종 리스트에 추가
    for i in range(len(gns_count)):
        sorted_nums += [GNS[i]] * gns_count[i]

    print(tc)
    print(*sorted_nums)
