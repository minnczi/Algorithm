from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = Counter(arr)
        return True if len(set(count_dict.keys())) == len(set(count_dict.values())) else False
