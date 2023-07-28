# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        big = head
        small = head
        while big is not None and big.val < x:
            big = big.next
        while small is not None and small.val >= x:
            small = small.next
        if small is None or big is None:
            return head
        
        small_ptr = small
        big_ptr = big
        if small==head:
            while small_ptr.next!=big:
                small_ptr = small_ptr.next
            small_ptr.next = big.next
        if big==head:
            while big_ptr.next!=small:
                big_ptr = big_ptr.next
            big_ptr.next = small.next
        while small_ptr is not None and big_ptr is not None:
            if small_ptr.next is not None:
                if small_ptr.next.val < x:
                    small_ptr = small_ptr.next
                    big_ptr.next = small_ptr.next
                else:
                    big_ptr = big_ptr.next
                    small_ptr.next = big_ptr.next
            else:
                small_ptr.next = big
                break
        return small


        