# arr의 item 개수를 변경해 가면서 실행해 보세요.
arr = [3, 6, 7, 1] 

n = len(arr) 		# n : 원소의 개수
# print(range(1 << n))
# print(arr)
for i in range(1 << n): 	# 1<<n : 부분 집합의 개수
    bi = bin(i)[2:]  # 앞의 '0b' 제거
    bi = '0'*(4-len(bi)) + bi
    my_list = ['%s' % bi]
    for j in range(n): 	    # 원소의 수만큼 비트를 비교
        if i & (1 << j): 	# i의 j번째 비트가 1이면 j번째 원소 출력
            print(i & (1 << j))
            my_list.append(arr[j])
    print(my_list)