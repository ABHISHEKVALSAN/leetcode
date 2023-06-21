# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, is_root):
        if isinstance(root.val,list):
            if is_root:
                return root.val[0]
            else:
                return root.val[1]
        if root.left is None:
            if root.right is None:
                root.val = [root.val,max(0,root.val)]
            else:
                r_sum_f = self.solve(root.right,False)
                r_sum_t = self.solve(root.right,True)
                root.val = [max(root.val,root.val+r_sum_f,r_sum_t),max(0,root.val+r_sum_f)]
        else:
            if root.right is None:
                l_sum_f = self.solve(root.left,False)
                l_sum_t = self.solve(root.left, True)
                root.val = [max(root.val,root.val+l_sum_f,l_sum_t),max(0,root.val+l_sum_f)]
            else:
                l_sum_f = self.solve(root.left, False)
                l_sum_t = self.solve(root.left,True)
                r_sum_f = self.solve(root.right, False)
                r_sum_t= self.solve(root.right,True)
                root.val = [
                                max(
                                    root.val,
                                    root.val+l_sum_f+r_sum_f,
                                    r_sum_t,
                                    l_sum_t),
                                max(
                                    0,
                                    root.val+max(l_sum_f,r_sum_f))]
        if is_root:
            return root.val[0]
        else:
            return root.val[1]

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.solve(root,True)
