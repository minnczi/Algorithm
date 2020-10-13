def solution(citations):
    # up = h번 이상 인용된 논문
    up = 1
    citations.sort(reverse=True)
    for i in citations:
        if up == i:
            return i
        elif up > i:
            return up-1
        else:
            up += 1
    return len(citations)