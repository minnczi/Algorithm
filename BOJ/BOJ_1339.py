from itertools import permutations

N = int(input())
words = [input() for _ in range(N)]
letters = []
nums = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

for w in words:
    letters.extend(w)

letters = list(set(letters))
nums = nums[:len(letters)]
perm = permutations(nums, len(nums))
ans = 0

for p in perm:
    dict = {}
    i = 0
    for l in letters:
        dict[l] = p[i]
        i += 1
    temp_sum = 0
    for w in words:
        num = ''
        for wl in w:
            num += dict[wl]
        temp_sum += int(num)
    ans = max(ans, temp_sum)

print(ans)