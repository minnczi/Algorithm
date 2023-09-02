class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_index = -1
        left_sum = 0
        right_sum = sum(nums[1:])

        if left_sum == right_sum:
            return 0

        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                pivot_index = i
                break
        return pivot_index
