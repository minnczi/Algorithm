class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            ["M", 1000],
            ["CM", 900],
            ["D", 500],
            ["CD", 400],
            ["C", 100],
            ["XC", 90],
            ["L", 50],
            ["XL", 40],
            ["X", 10],
            ["IX", 9],
            ["V", 5],
            ["IV", 4],
            ["I", 1]
        ]

        idx = 0
        roman = []
        while num > 0:
            if num >= romans[idx][1]:
                num -= romans[idx][1]
                roman.append(romans[idx][0])
            else:
                idx += 1
        return ''.join(roman)