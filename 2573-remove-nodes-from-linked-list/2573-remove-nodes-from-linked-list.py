# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev_ll(head):
            if head is None or head.next is None:
                return head
            prev = None
            curr = head
            nxt  = head.next

            while nxt is not None:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next
            curr.next = prev
            return curr
        head = rev_ll(head)
        itr = head
        max_val = head.val
        while itr.next is not None:
            if itr.next.val < max_val:
                itr.next = itr.next.next
            else:
                itr = itr.next
                max_val = itr.val
        return rev_ll(head)
