"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def solve(node):
            if node is None:
                return None
            new_node = Node(node.val,None,None)
            new_node.next = solve(node.next)
            return new_node
        def solve_random(node):
            otr = head
            ntr = head_new
            random_node = node.random
            while otr is not None and ntr is not None:
                if otr==random_node:
                    return ntr
                otr = otr.next
                ntr = ntr.next
            return None

        head_new = solve(head)
        itr_new = head_new
        itr_old = head
        while itr_old is not None and itr_new is not None:
            itr_new.random = solve_random(itr_old)
            itr_old = itr_old.next
            itr_new = itr_new.next
        return head_new
