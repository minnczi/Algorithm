# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            # storing the current next in the next_node variable
            next_node = curr.next
            # pointing the current head to the reverse direction
            curr.next = prev
            # moving curr and prev by 1 (to move on to the next nodes)
            prev, curr = curr, next_node
        return prev
