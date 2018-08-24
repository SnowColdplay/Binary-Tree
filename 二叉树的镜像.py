"操作给定的二叉树，将其变换为源二叉树的镜像。"

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root:
            root.left,root.right=root.right,root.left
            if root.left:
                self.Mirror(root.left)
            if root.right:
                self.Mirror(root.right)
        return root