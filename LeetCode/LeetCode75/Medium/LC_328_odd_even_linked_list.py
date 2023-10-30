class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        even_head = head.next
        odd_now = head
        even_now = head.next
        next_node = head.next.next
        idx = 3

        while next_node:
            if idx % 2:
                odd_now.next = next_node
                odd_now = odd_now.next
            else:
                even_now.next = next_node
                even_now = even_now.next

            next_node = next_node.next
            idx += 1

        even_now.next = None
        odd_now.next = even_head

        return head
