class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        int_num = 0
        prev = 0

        for i in range(len(s)-1, -1, -1):
            current = int(roman_dict[s[i]])
            if current >= prev:
                int_num += current
            else:
                int_num -= current
            prev = current
        
        return int_num