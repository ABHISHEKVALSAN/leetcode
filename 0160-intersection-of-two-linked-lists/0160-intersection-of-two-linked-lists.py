# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA is None:
            return None
        if headB is None:
            return None

        n1 = 0
        itr = headA
        while itr is not None:
            itr = itr.next
            n1+=1
        n2 = 0
        itr = headB
        while itr is not None:
            itr = itr.next
            n2+=1
        itr1 = headA
        itr2 = headB
        print(n1,n2)
        if n1 >= n2:
            i = 0
            while i < (n1-n2) and itr1 is not None:
                itr1 = itr1.next
                i+=1
        else:
            i = 0
            while i < (n2-n1) and itr2 is not None:
                itr2 = itr2.next
                i+=1
        while itr1 is not None and itr2 is not None:
            if itr1==itr2:
                return itr1
            else:
                itr1 = itr1.next
                itr2 = itr2.next
        return None
