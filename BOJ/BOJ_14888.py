N = int(input())
numbers = list(map(int, input().split()))
signs = list(map(int, input().split()))
results = []
calc = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y if x > 0 and y > 0 else -(-x // y)
]

def dfs(idx, total):
    
    if idx == N:
        results.append(total)
        return
    
    for i in range(4):
        if signs[i] > 0:
            signs[i] -= 1
            dfs(idx+1, calc[i](total,numbers[idx]))
            signs[i] += 1

dfs(1, numbers[0])
print(max(results))
print(min(results))