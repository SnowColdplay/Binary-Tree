'题目描述：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def HasSubtree(self, pRoot1, pRoot2):
        result=False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val==pRoot2.val:
                result=self.isEqual(pRoot1,pRoot2)
        if not result:
            result=self.HasSubtree(pRoot1.left,pRoot2)
        if not result:
            result=self.HasSubtree(pRoot1.right,pRoot2)
        return result
    
    def isEqual(self,p1,p2):
        if not p2:
            return True
        if not p1:
            return False
        if p1.val!=p2.val:
            return False
        return self.isEqual(p1.left,p2.left) and self.isEqual(p1.right,p2.right)
