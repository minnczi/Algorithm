"""
l = left
r = right
tl = tmp left
tr = tmp right
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, tl, r, tr = 0, 0, len(height)-1, len(height)-1
        area = (r-l) * min(height[l], height[r])

        while tl < tr:
            tmp_area = (tr-tl) * min(height[tl], height[tr])
            # 이동한 포인터 인덱스로 계산한 넓이가 더 넓을경우 l, r 값 갱신
            if tmp_area > area:
                l, r, area = tl, tr, tmp_area
            # 포인터 인덱스 이동
            if height[tl] <= height[tr]:
                tl += 1
            else:
                tr -= 1

        return area
