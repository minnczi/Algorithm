# BOJ_6137 문자열 생성
"""
f = front
b = back
tf = temporary front
tb = temporary back
N = 문자 갯수
S = 문자열 배열 (list)
T = 새로 만드는 문자열 (string)
"""

N = int(input())
S = [input() for _ in range(N)]
T = ''
f, tf, b, tb = 0, 0, N-1, N-1

while len(T) < N:
    # 가장 가운데까지 비교했는데도 사전 순서가 동일하다면
    # 예) abcba -> c까지 비교했는데 순서가 전부 동일
    # -> 앞 문자열을 추가하고 다음으로 넘어간다
    if tb <= tf:
        T += S[f]
        f += 1
    # f가 사전순으로 앞에 있으면
    elif S[tf] < S[tb]:
        T += S[f]
        f += 1
    # b가 사전순으로 앞에 있으면
    elif S[tb] < S[tf]:
        T += S[b]
        b -= 1
    # f == b라면
    else:
        tf, tb = tf+1, tb-1
        continue
    tf, tb = f, b

for i in range(len(T)):
    print(T[i], end="")
    if i % 80 == 79:
        print("")
        