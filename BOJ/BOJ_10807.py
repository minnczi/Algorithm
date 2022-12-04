import sys
input = sys.stdin.readline

counts = [0] * 201

N = int(input().rstrip())

num_list = list(map(int, input().rstrip().split()))
counts = [0] * 201

for num in num_list:
    counts[num] += 1

target_num = int(input().rstrip())
print(counts[target_num])