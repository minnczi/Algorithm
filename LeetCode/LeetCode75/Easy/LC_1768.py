class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short_len = min(len(word1), len(word2))
        long_len = max(len(word1), len(word2))

        word = ''
        for i in range(short_len):
            word += word1[i] + word2[i]
        
        word += word1[short_len:long_len] + word2[short_len:long_len]
        return word
        ````