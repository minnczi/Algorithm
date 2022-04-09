N = int(input())
students = {}
for _ in range(N):
    name, *scores = input().split()
    students[name] = list(map(int, scores))

result = sorted(students.keys(), key=lambda x: (-students[x][0], students[x][1], -students[x][2], x))
for name in result:
    print(name)