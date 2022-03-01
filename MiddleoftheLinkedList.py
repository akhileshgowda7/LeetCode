# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def middleNode(self, head: ListNode)->ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


start=ListNode(0)
start.next = ListNode(1)
start.next.next =ListNode(2)
start.next.next.next = ListNode(3)
start.next.next.next.next = ListNode(4)
start.next.next.next.next.next = ListNode(5)
