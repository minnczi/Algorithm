T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m, n = map(int, input().split())
    
    input_array = []
    # input 받는 부분
    for i in range(m):
        lst = list(map(int, input().split()))
        input_array.append(lst)
    
    maximum = 0
    for i in range(m-n+1):
        for j in range(m-n+1):
            total = 0
            for a in range(i, i+n):
                for b in range(j, j+n):
                    print(input_array[a][b])
                    total += input_array[a][b]
            if total > maximum:
                maximum = total
    print(f'#{test_case+1} {maximum}')

                