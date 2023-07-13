# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0:
            return head
        n = 0
        itr = head
        while itr is not None:
            n+=1
            itr = itr.next
        if n==0 or n==1:
            return head
        k = k%n
        if k==0:
            return head
        k = n - k

        i = 0
        itr = head
        while i < k-1 and itr is not None:
            itr = itr.next
            i+=1
        ntr = itr.next
        itr.next = None
        head1 = ntr
        while ntr is not None and ntr.next is not None:
            ntr = ntr.next
        ntr.next = head
        return head1