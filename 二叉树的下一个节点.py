"题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针"
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
"分情况讨论"
"1.有右子树，返回右子树的第一个左节点"
"2.没有右子树：2.1 是父节点的左节点：返回父节点 2.2 是父节点的右节点：往上找，知道找到是父节点的左节点，返回父节点"
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode.next.left==pNode:
                    pNode=pNode.next
                    return pNode
                if pNode.next.right==pNode:
                    pNode=pNode.next
            return None