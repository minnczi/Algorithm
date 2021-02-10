T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))

    # max와 min을 찾은다음 인덱스 값을 구해서 리스트에서 팝!
    num_list.pop(num_list.index(max(num_list)))
    num_list.pop(num_list.index(min(num_list)))

    average = round(sum(num_list) / len(num_list))

    print(f'#{test_case} {average}')