"题目：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。"
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.isduichen(pRoot.left,pRoot.right)

    def isduichen(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val!=right.val:
            return False
        if left.val==right.val:
            return self.isduichen(left.left,right.right) and self.isduichen(left.right,right.left)


