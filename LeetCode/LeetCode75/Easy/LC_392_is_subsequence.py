class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx, tidx = 0, 0
        S, T = len(s), len(t)

        while sidx < S and tidx < T:
            if s[sidx] == t[tidx]:
                sidx += 1
            tidx += 1

        return sidx == S
