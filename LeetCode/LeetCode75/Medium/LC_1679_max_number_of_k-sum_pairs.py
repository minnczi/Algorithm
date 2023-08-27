from collections import Counter

"""
Runtime: 98.96%
Memory: 24.64%
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)

        # 더했을때 k가 되는 두 숫자의 조합중 작은 수의 후보 리스트
        # k/2값은 예외처리 예정으로 일부러 제외
        keys = [i for i in count.keys() if i < k/2]

        ans = 0
        # i 라는 값이 있을때 더했을때 k가 나올수 있는 상대값은 k-i이므로
        # i와 k-i의 갯수를 구해, 그 둘중 최소값 만큼 k값의 조합을 만들수 있다
        for i in keys:
            ans += min(count[i], count[k-i])

        # 다만 i가 정확히 k/2인경우, i를 두번 사용해야 k를 만들수 있기 때문에 이 경우만 예외 처리한다
        if k % 2 == 0:
            ans += count[k//2]//2

        return ans
