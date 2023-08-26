from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [True if (c + extraCandies) >=
                  max_candies else False for c in candies]
        return result
