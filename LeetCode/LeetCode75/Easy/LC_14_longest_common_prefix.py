class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            if len(prefix) == 0:
                return prefix

            for i in range(min(len(prefix), len(s))):
                if prefix[i] != s[i]:
                    prefix = s[0:i]
                    break
            else:
                prefix = prefix if len(prefix) < len(s) else s
                
        return prefix