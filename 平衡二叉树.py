class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def maxdepth(self, root):
        if not root:
            return 0
        else:
            return max(self.maxdepth(root.left),self.maxdepth(root.right))+1

    def is_balance(self,root):
        if not root:
            return True
        if abs(self.maxdepth(root.left)-self.maxdepth(root.right))>1:
            return False
        return self.is_balance(root.left) and self.is_balance(root.right)





    