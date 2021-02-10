import sys
sys.stdin = open("sample_input_minmax.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    first = nums[0]
    second = nums[1]

    if first > second:
        maximum, minimum = first, second
    else:
        maximum, minimum = second, first

    for num in nums[2:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    result = maximum - minimum
    print("#%d %d" % (t+1, result))

