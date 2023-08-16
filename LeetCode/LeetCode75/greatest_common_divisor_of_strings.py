class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        gcd = ""
        for i in range(1, min(len1, len2)+1):
            if str1[0:i] == str2[0:i]:
                temp = str1[0:i]
                # check if temp divides both str1 and str2
                if temp * (len1 // i) == str1 and temp * (len2 // i) == str2:
                    gcd = temp
            else:
                break

        return gcd
