# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            ptr1 = list1
            ptr2 = list2
        else:
            ptr1 = list2
            ptr2 = list1
        ans = ptr1

        while ptr1 is not None and ptr2 is not None:
            print(ptr1.val, ptr2.val)
            if ptr1.next is None:
                ptr1.next = ptr2
                break
            if ptr1.next is not None and ptr1.next.val == ptr1.val:
                ptr1 = ptr1.next
                continue
            if ptr1.val <= ptr2.val and ptr1.next.val <= ptr2.val:
                ptr1 = ptr1.next
                continue
            else:
                temp = ptr2
                ptr2 = ptr2.next
                temp.next = ptr1.next
                ptr1.next = temp
                ptr1 = ptr1.next

        return ans
            


