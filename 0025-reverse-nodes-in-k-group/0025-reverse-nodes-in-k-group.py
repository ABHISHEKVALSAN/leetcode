# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def print_ll(self, ll):
        while ll is not None:
            print(ll.val,end=' ')
            ll = ll.next
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        head_org = head
        itr = head
        n = 0
        while itr is not None:
            itr = itr.next
            n+=1
        node_groups = n//k
        itr = head
        if node_groups >= 1:
            kh = k
            while kh > 1:
                head = head.next
                kh-=1

        kh = k
        itr_end = itr
        while node_groups >=1 and kh > 1:
            itr_end = itr_end.next
            kh-=1

        while node_groups>0:
            itr_prev = itr_end.next
            itr_next = itr.next

            kh = k
            while kh > 0:
                itr.next = itr_prev
                itr_prev = itr
                itr = itr_next
                if itr_next is not None:    
                    itr_next = itr_next.next
                kh-=1

            node_groups-=1
            if node_groups==0:
                return head
            
            while itr_prev.next != itr:
                itr_prev = itr_prev.next

            itr_end = itr
            kh = k
            while kh>1:
                itr_end = itr_end.next
                kh-=1

            itr_prev.next = itr_end
            
        return head