# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        while head is not None and head.next is not None and head.val == head.next.val:
            val = head.val
            while head is not None and head.val==val:
                head = head.next
        if head is None:
            return head
        itr = head
        nxt = head.next
        while nxt is not None:
            if nxt.next is not None and nxt.val == nxt.next.val:
                val = nxt.val
                while nxt is not None and nxt.val == val:
                    nxt = nxt.next
            else:
                itr.next = nxt
                itr = itr.next
                if nxt is not None:
                    nxt = nxt.next
        itr.next = nxt
        return head