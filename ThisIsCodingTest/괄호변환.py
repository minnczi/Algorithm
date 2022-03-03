# 문자열 뒤집기 함수
def flip_string(u):
		# 맨 앞과 맨 뒤 문자열 자르기
    u = u[1:len(u)-1]
		# 괄호 방향 뒤집기
    new_u = ''
    for i in u:
        if i == '(':
            new_u += ')'
        else:
            new_u += '('
    return new_u
    
# 메인 함수
# 올바른 문자열 만들기
def find_right_string(w):
    
    if not w:
        return w
    
    cnt = 0
    right = True
    u, v = '', ''
    for i in range(0, len(w)):
        if w[i] == '(':
            cnt += 1
            
        else:
            cnt -= 1
            if cnt < 0:
                right = False
        
        if cnt == 0:
            u, v = w[:i+1], w[i+1:]
            break
    
    if right:
        return u + find_right_string(v)
    else:
        return '(' + find_right_string(v) + ')' + flip_string(u)
    
    
def solution(p):
    answer = find_right_string(p)
    return answer