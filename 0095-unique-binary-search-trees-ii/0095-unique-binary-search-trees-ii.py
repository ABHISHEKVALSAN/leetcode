# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(nums):
            if len(nums)==0:
                yield None
            if len(nums)==1:
                yield TreeNode(nums[0],None,None)
            else:
                i = 0
                while i < len(nums):
                    for left_tree in solve(nums[:i]):
                        for right_tree in solve(nums[i+1:]):
                            yield TreeNode(nums[i],left_tree,right_tree)
                    i+=1
        result = []
        for bst in solve(range(1,n+1)):
            result.append(bst)
        return result