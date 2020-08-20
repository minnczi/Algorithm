def solution(n, lost, reserve):
    answer = 0
    received = []
    for i in range(1,n+1):
        if i not in (lost+reserve):
            answer += 1
            print("Y", i)
        elif i in reserve:
            if i in lost:
                answer += 1
            elif (i-1) in lost and (i-1) not in (received + reserve):
                answer += 2
                received.append(i-1)
            elif (i+1) in lost and (i+1) not in (received + reserve):
                answer += 2
                received.append(i+1)
            else:
                answer +=1
            print("R", i)

    return answer