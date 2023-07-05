# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        prev = None
        curr = head
        nxt = head.next

        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next

        curr.next = prev
        prev.next = self.swapPairs(nxt)

        return curr


