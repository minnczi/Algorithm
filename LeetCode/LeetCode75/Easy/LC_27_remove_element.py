class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            n = nums.pop()
            if n != val:
                nums.insert(0, n)
                k += 1
        return k