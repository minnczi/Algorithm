import sys

sys.stdin = open("babygin_input2.txt", "r")

T = int(input())

for t in range(1, T+1):
    arr = []
    arr.extend(str(input()))
    print(arr)