T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    words = input() # tc 입력: KOREAKOREAKOREAKOREAKOREAKOREA
    cnt = 0
    for i in range(1, len(words)+1):
        if words[0:i] == words[i:2*i]:
            cnt = i
            # print(cnt)
            break
        else:
            pass
    print(f'#{test_case} {cnt}')
                  