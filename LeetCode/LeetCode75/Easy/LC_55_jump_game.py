# idx = current position
# i = potential next position
# nums[i] = how many steps I can jump from the next position
# from idx, find the one where i + nums[i] is the greatest and move to that position
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        while True:
            # immediately stop if you can't move at all from the current position
            if nums[idx] == 0 and idx < len(nums)-1:
                return False

            # the distance from current number -> next number + how many steps you can go from that next number
            max_reach = 0
            next_idx = -1
            for i in range(idx, idx+nums[idx]+1):
                if i >= len(nums)-1:
                    return True

                if (i+nums[i]) >= max_reach:
                    next_idx = i
                    max_reach = i + nums[i]
            idx = next_idx