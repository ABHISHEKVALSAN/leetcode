# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i,l in enumerate(lists):
            if l is not None:
                heapq.heappush(heap,[l.val,i])
        if not heap:
            return

        val, i = heapq.heappop(heap)
        head = lists[i]
        fl_ptr = head
        lists[i] = lists[i].next
        if lists[i] is not None:
            heapq.heappush(heap,[lists[i].val,i])
        
        while heap:
            val, i = heapq.heappop(heap)
            fl_ptr.next = lists[i]
            fl_ptr = fl_ptr.next
            lists[i] = lists[i].next

            if lists[i] is not None:
                heapq.heappush(heap,[lists[i].val,i])
        return head

