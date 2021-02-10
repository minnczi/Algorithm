T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = [[1], [1, 1]]
    prev = [1, 1]

    if n == 1:
        print(1)
        break

    elif n == 2:
        print(1)
        print(1, " ", 1)
        break

    for i in range(2, n): # 층
        lst = [1]
        for j in range(1, i): # list안에 있는 element
            num = prev[j] + prev[j-1]
            lst.append(num)
        lst.append(1)
        result.append(lst)
        prev = lst
    
    # 프린트 하는 구문
    print(f'#{test_case}')
    for lst in result:
        for elem in lst:
            print(elem, end=" ")
        print("")