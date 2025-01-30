from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        k = 0
        for i in range(len(nums)-1, -1, -1):
            if cnt[nums[i]] == 0:
                cnt[nums[i]] += 1
                k += 1
            else:
                nums.pop(i)
        return k