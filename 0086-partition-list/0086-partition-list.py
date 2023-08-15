# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        big = head
        small = head
        while small and small.val >= x:
            small = small.next
        while big and big.val <x:
            big = big.next
        if small is None or big is None:
            if small:
                return small
            else:
                return big

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
        
        while small_ptr and big_ptr:
            if small_ptr.next:
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


        