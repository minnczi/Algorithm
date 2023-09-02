class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, -1
        longest = -1
        zero_cnt = 0

        while right <= len(nums)-2:
            right += 1

            if nums[right] == 0:
                zero_cnt += 1

            if zero_cnt <= 1:
                longest += 1
                continue
            else:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

        return longest
