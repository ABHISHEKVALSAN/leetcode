# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = 0
        p = 1
        while l1 is not None:
            n1 = l1.val * p + n1
            p*=10
            l1 = l1.next
        
        n2 = 0
        p = 1
        while l2 is not None:
            n2 = l2.val * p + n2    
            p*=10
            l2 = l2.next

        ans = n1 + n2
        l3 = ListNode(ans%10)
        ans= ans//10

        itr = l3
        while ans>0:
            r = ans % 10
            itr.next = ListNode(r)
            ans = ans//10
            itr = itr.next

        return l3