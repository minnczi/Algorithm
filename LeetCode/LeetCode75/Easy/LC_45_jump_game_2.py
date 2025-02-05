class Solution:
    def jump(self, nums: List[int]) -> int:
        idx = 0
        jumps = 0
        while True:
            if idx == len(nums)-1:
                return jumps

            # the distance from current number -> next number + how many steps you can go from that next number
            max_reach = 0
            next_idx = -1
            jumps += 1
            for i in range(idx, idx+nums[idx]+1):
                if i >= len(nums)-1:
                    return jumps

                if (i+nums[i]) >= max_reach:
                    next_idx = i
                    max_reach = i + nums[i]
            idx = next_idx
