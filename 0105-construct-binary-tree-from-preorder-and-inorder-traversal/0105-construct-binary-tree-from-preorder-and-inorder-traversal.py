# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==len(inorder)==0:
            return 
        if len(preorder)==len(inorder)==1:
            return TreeNode(inorder[0],None,None)
        else:
            root = preorder[0]
            root_index = inorder.index(root)
            return TreeNode(
                        root,
                        self.buildTree(
                                    preorder[1:root_index+1],
                                    inorder[:root_index],
                                ),
                        self.buildTree(
                                    preorder[root_index+1:],
                                    inorder[root_index+1:],
                                )
                        ) 