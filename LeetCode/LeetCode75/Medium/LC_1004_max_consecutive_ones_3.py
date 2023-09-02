"""
Approach
left = start idx of an array
right = end idx of an array

1. Start at left = 0, right = 0
2. Keep expanding the length of an array while the number of 0's <= k
and update the max length of an array
3. When num_0's > k shift an array (left and right) by 1
4. Repeat 2-3 until we reach the end of the original list
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, -1
        max_ones = 0
        zero_cnt = 0

        while right <= len(nums)-2:
            right += 1
            if nums[right] == 0:
                zero_cnt += 1

            # num_zero <= k
            if zero_cnt <= k:
                max_ones += 1
                continue
            # num_zero > k
            else:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

        return max_ones
