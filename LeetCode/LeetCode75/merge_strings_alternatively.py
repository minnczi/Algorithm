class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        max_len = max(len(word1), len(word2))
        idx = 0
        ans = ""
        while idx < max_len:
            if idx < len(word1):
                ans += word1[idx]
            if idx < len(word2):
                ans += word2[idx]
            idx += 1
        return ans