answer = 0


def dfs(numbers, target, idx, current_value):
    global answer
    if idx == len(numbers) and current_value == target:
        answer += 1
        return
    if idx == len(numbers):
        return

    dfs(numbers, target, idx + 1, current_value + numbers[idx])
    dfs(numbers, target, idx + 1, current_value - numbers[idx])


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer
