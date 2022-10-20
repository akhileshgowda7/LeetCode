class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if head is None:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr2 = slow
                ptr1 = head
                while ptr1!=ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1
        return None