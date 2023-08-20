import sys
sys.stdin = open('9935_input.txt', 'r')
input = sys.stdin.readline

word = input().rstrip()
bomb = list(input().rstrip())

L = len(bomb)
stack = []

for i in word:
    stack.append(i)
    # stack의 탑이 폭발 문자의 끝 문자랑 같다면
    if i == bomb[-1]:
        # 전체 문제 체크 (-m 전 인덱스부터 지금 인덱스까지 체크)
        if stack[-L:] == bomb:
            # 같다면 제거
            del stack[-L:]

if stack:
    print("".join(stack).rstrip())
else:
    print("FRULA")