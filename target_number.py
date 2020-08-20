answer = 0

def DFS(numbers, target, idx, current_value):
    global answer
    if (idx == len(numbers) and current_value == target):
        answer += 1
        return
    if (idx == len(numbers)):
        return

    DFS(numbers, target, idx + 1, current_value + numbers[idx])
    DFS(numbers, target, idx + 1, current_value - numbers[idx])


def solution(numbers, target):
    DFS(numbers, target, 0, 0)
    return answer