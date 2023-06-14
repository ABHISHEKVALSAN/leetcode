# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        itr = head
        while itr is not None:
            leng+=1
            itr = itr.next

        if leng <= 1:
            return None
    
        n = leng - n + 1
        itr = head
        
        if n==1:
            itr = itr.next
            return itr

        i = 1
        while i < n - 1:
            itr = itr.next
            i+=1 

        temp = itr.next
        itr.next = temp.next

        return head
        