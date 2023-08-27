class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum, temp_sum = sum(nums[0:k]), sum(nums[0:k])
        for i in range(0, n-k):
            temp_sum = temp_sum - nums[i] + nums[i+k]
            max_sum = temp_sum if temp_sum > max_sum else max_sum
        return max_sum / k
