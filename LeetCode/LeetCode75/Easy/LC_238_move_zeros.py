"""
Approach
Starting from the end of the list, pop all 0's from the list and count the number of 0's
Append the cnt * [0] at the end of the list
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                cnt += 1
        nums += [0] * cnt
