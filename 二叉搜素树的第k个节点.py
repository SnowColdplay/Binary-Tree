"题目：给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4"
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"知识点：二叉搜索树中序遍历的结果，就是按顺序的"
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        result=[]
        self.inorder(pRoot,result)
        if len(result)<k:
            return None
        return result[k-1]
    def inorder(self,root,result):
        if not root:
            return None
        if root.left:
            self.inorder(root.left,result)
        result.append(root.val)
        if root.right:
            self.inorder(root.right,result)


