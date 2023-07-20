# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left==right:
            return head
        k = 1
        left_prev = None
        itr = head
        while k<left:
            left_prev = itr
            itr = itr.next
            k+=1

        end_node = itr
        while k <= right:
            end_node = end_node.next
            k+=1
        #print('en',end_node.val)
        right_prev = end_node
        curr = itr
        nxt = itr.next

        k = left
        while k<right and nxt!=end_node:
            if right_prev is None:
                print(None,curr.val,nxt.val)
            else:
                print(right_prev.val,curr.val,nxt.val)
            curr.next = right_prev
            right_prev = curr
            curr = nxt
            nxt = nxt.next
            k+=1
        curr.next = right_prev
        if left_prev is not None:
            left_prev.next = curr
            return head
        else:
            return curr
