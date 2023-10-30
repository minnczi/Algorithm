from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        # find the length of the entire list
        while node:
            length += 1
            node = node.next
        if length == 1:
            return None

        # find the middle node
        mid = length // 2
        idx = 0
        prev = None
        curr = head
        while True:
            # delete the middle node
            # and link prev directly to next
            if idx == mid:
                next = curr.next
                prev.next = next
                break
            curr, prev = curr.next, curr
            idx += 1
        return head

    def deleteMiddleTwoPointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
