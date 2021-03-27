import sys
sys.stdin = open('1931_input.txt', 'r')

"""
접근법 (다음 미팅 고르기):
현재 미팅이 끝나는 시간보다 늦게 시작하는 미팅들 중에서
끝나는 시간이 가장 빠른 미팅을 고른다

1. 미팅을 끝나는 시간 순으로 정렬한다
2. 현재 미팅보다 뒤에 있는 미팅들 중에 미팅의 시작 시작이 현재 미팅의 끝나는
시간보다 뒤에 있는 미팅이 있다면, 그 미팅이 다음 미팅이 되고 cnt += 1

변수:
idx = 현재 회의의 인덱스
ce = current end
ns = next start
ne = next end
"""

N = int(input())

meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings = sorted(meetings, key=(lambda x: (x[1], x[0])))

cnt = 1
ce = meetings[0][1]
idx = 1

while idx < len(meetings):
    if meetings[idx][0] >= ce:
        cnt += 1
        ce = meetings[idx][1]
    idx += 1

print(cnt)