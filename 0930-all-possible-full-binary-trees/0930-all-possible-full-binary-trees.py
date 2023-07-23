# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        result = []
        if n==1:
            return [TreeNode(0,None,None)]
        elif n==2:
            return []
        elif n>=3:
            result = []
            i = 1
            while i<n-1:
                left = self.allPossibleFBT(i)
                right = self.allPossibleFBT(n-i-1)
                l = 0
                while l<len(left):
                    r = 0
                    while r<len(right):
                        result.append(TreeNode(0,left[l],right[r]))
                        r+=1
                    l+=1
                i+=1
            return result
        