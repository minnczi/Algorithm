class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1,0,-1):
            if (target-numbers[i]) in numbers:
                return [numbers.index(target-numbers[i])+1, i+1]