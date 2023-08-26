from collections import Counter


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        answer = []
        for num in nums:
            counter[num] = counter[num] - 1

            product = 1
            for k, v in counter.items():
                product *= (k**v)
            answer.append(product)
            counter[num] = counter[num] + 1

        return answer
