from collections import defaultdict


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = defaultdict(int)
        vowels['a'], vowels['e'], vowels['i'], vowels['o'], vowels['u'] = 1, 1, 1, 1, 1

        max_vowels = 0
        for i in s[0:k]:
            max_vowels += vowels[i]

        prev_vowels = max_vowels
        for i in range(0, len(s)-k):
            prev_vowels = prev_vowels - vowels[s[i]] + vowels[s[i+k]]
            max_vowels = max(prev_vowels, max_vowels)

        return max_vowels
