"""
이것이 코딩테스트다
Greedy: 곱하기 혹은 더하기

### 문제
N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

### 입력 조건
- 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.(1 <= N <= 1,000, 1 <= M <= 10)
- 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다.(1 <= K <= M)

### 출력 조건
- 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.
"""

N, M = map(int, input().split())
balls = list(map(int, input().split()))
answer = 0

# 무게가 idx인 공의 갯수를 저장하는 배열
# ball_cnt[1] = 무게가 1인 공의 갯수
ball_cnt = [0] * (M+1)

for b in balls:
    ball_cnt[b] += 1

for i in range(1, M):
    answer += ball_cnt[i] * sum(ball_cnt[i+1:])

print(answer)