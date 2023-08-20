"""
s = 문자열
n = 몇글자 단위로 쪼갤지
l = 문자열의 길이
prev = 이전 n개의 문자
now = 현재 n개의 문자
rep = 현재 문자가 몇번 반복됐는지
cnt = 압축 후 문자열 길이
"""

def compress(s, n, l):
    prev = s[:n]
    cnt = n
    rep = 1
    for i in range(1, l//n):
        now = s[n*i:n*(i+1)]
        if prev != now:
            cnt += n
            rep = 1
        else:
            # 이번에 처음 반복되는 문자거나 반복횟수의 자리수가 바뀌면 한자리 추가
            if rep in [1, 10, 100, 1000]:
                cnt += 1
            rep += 1
        prev = now
    return cnt
        
    

def solution(s):
    l = minimum = len(s)
    # 어차피 문자열의 길이가 l//2보다 크면 반복 자체가 될 수 없기 때문에 l//2까지만 체크
    for n in range(1, l//2+1):
        cnt = compress(s, n, l)
        # 남는 문자열이 있을 경우 처리
        if l % n:
            cnt += (l % n)
        if cnt < minimum:
            minimum = cnt
    return minimum