# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == len(postorder)==0:
            return 
        elif len(inorder) == len(postorder)==1:
            return TreeNode(inorder[0],None,None)
        else:
            root = postorder[-1]
            root_index = inorder.index(root)
            return TreeNode(
                root,
                self.buildTree(
                    inorder[:root_index],
                    postorder[:root_index]),
                self.buildTree(
                    inorder[root_index+1:],
                    postorder[root_index:-1])
            )