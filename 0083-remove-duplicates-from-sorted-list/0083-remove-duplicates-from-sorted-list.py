# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        itr = head
        while itr.next is not None:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        return head