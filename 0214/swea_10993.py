# 파이썬은 답 체크가 안되서 답 확인을 못해봐써ㅠㅠ
import sys
sys.stdin = open('10993_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cities = []
    result = []

    # input 받기
    for _ in range(N):
        cities.append(list(map(int, input().split())))
    
    for j in range(N): # 영향을 받는 쪽
        impact_list = []
        for i in range(N): # 영향을 주는 쪽
            try:
                impact = cities[i][2] / ((cities[j][0]-cities[i][0])**2 + (cities[j][1]-cities[i][1])**2)
            except:
                impact = 0
                
            if impact > cities[j][2]:
                impact_list.append(i+1)

        if len(impact_list) >= 2:
            result.append('D')
        elif len(impact_list) == 0:
            result.append('K')
        else:
            result.append(str(impact_list[0]))
        
        print('#%d %s' % (tc, " ".join(result)))