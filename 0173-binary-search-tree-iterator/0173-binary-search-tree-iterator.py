# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.result = []
        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                self.result.append(root.val)
                if root.right:
                    inorder(root.right)
        inorder(root)
        self.ptr = 0


    def next(self) -> int:
        val = self.result[self.ptr]
        self.ptr+=1
        return val
        

    def hasNext(self) -> bool:
        return self.ptr<len(self.result)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()