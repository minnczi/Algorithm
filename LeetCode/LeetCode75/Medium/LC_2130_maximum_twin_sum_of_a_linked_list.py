# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 전체 리스트의 길이를 구한다 (N)
        cnt = 0
        node = head
        while node:
            cnt += 1
            node = node.next

        # 전체 pair의 sum을 구할 배열을 초기화한다 (length = cnt//2)
        # 예) N = 10이라면 5쌍의 twin sum이 있으니 twin_sum = [0,0,0,0,0]으로 초기화
        sum_list = [0] * (cnt//2)

        # 3-1: First half의 원소들을 배열에 순차적으로 더한다
        # 예) twin_sum의 0번째 원소에서부터 순서대로 숫자를 더한다
        node = head
        for i in range(cnt//2):
            sum_list[i] = node.val
            node = node.next

        # 3-2: Second half의 원소들을 배열에 역순으로 더한다
        # 예) twin_sum[-1] 부터 거꾸로 배열을 순회하면서 twin_sum에 있던 숫자와 새로운 숫자를 더한다
        for i in range(1, cnt//2+1):
            sum_list[-i] += node.val
            node = node.next

        return max(sum_list)
