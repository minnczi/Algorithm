#link to the problem: https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        for row in board:
            if row[move-1] != 0:
                current = row[move-1]
                row[move-1] = 0
                if basket == [] or basket[-1] != current:
                    basket.append(current)
                    break
                else:
                    basket.pop()
                    answer += 2
                    break
    return answer