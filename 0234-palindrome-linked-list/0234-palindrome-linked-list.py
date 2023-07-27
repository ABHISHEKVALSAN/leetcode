# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(h):
            if h is None or h.next is None:
                return h
            prev = None
            curr= h
            nxt = h.next
            while nxt is not None:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next
            curr.next = prev
            return curr

        itr = head
        n = 0
        while itr is not None:
            itr = itr.next
            n+=1
        print(n)
        n = (n+1)//2
        prev = None
        itr = head
        while n>0:
            prev = itr
            itr = itr.next
            n-=1
        prev.next = None
        itr1 = head
        itr2 = reverse(itr)
        while itr1 is not None and itr2 is not None:
            if itr1.val!=itr2.val:
                return False
            itr1 = itr1.next
            itr2 = itr2.next
        return True
        
