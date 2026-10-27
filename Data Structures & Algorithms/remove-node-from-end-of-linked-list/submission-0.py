# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # Dummy node before the head
        slow = dummy                # Slow pointer starts at dummy
        fast = dummy                # Fast pointer starts at dummy

        for _ in range(n):          # Move fast n steps ahead
            fast = fast.next

        while fast.next:            # Move both until fast reaches the last node
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  # Skip the node to delete

        return dummy.next       
        