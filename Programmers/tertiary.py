def solution(n):
    if n <= 2:
        return n
    else:
        #3진법으로 바꾸기
        quotient = n // 3
        remainder = n % 3
        tertiary = str(remainder) 
        while quotient > 2:
            remainder = quotient % 3
            quotient = quotient // 3
            tertiary += str(remainder)
        tertiary += str(quotient)

    #다시 2진법으로 바꾸기
    answer = 0
    for i in range (0, len(tertiary)):
        answer += int(tertiary[i]) * (3**(len(tertiary)-i-1))

    return answer
