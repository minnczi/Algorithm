import sys
sys.stdin = open('4865_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # str1은 한글자씩 리스트 형태로, str2는 스트링 형태로 받기
    str1_list = []
    str1_list.extend(input())
    str2 = input()

    # 중복 제거
    str1_list = set(str1_list)
    # str1에 나오는 알파벳의 갯수를 셀 dict 만들기
    count_dict = dict.fromkeys(str1_list, 0)

    # count dict 안에 있는 글자수를 센다
    # 만약 count dict 안에 없는 글자가 나오면 except문에서 처리해서 패스한다
    for i in str2:

        if KeyError:
            count_dict[i] += 1
        # try:
        #     count_dict[i] += 1
        # except:
        #     continue
        # count_dict[i] = count_dict.get(i, -1) + 1 
    # max값 찾기
    result = max(count_dict.values())
    print("#%d %d" % (tc, result))