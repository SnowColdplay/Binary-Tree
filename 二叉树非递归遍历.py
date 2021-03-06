class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    "先序遍历"
    def pre(self,root):
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    "中序遍历"
    def inorder(self,root):
        result=[]
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                "前面是root=root.left，保证先弹出的是左子树"
                "然后root=root.right，如果为空，说明到了最后，继续弹出，是当前节点的父节点"
                "如果root=root.right不是空，将root.right加入stack,之后弹出，是当前节点的右节点"
                result.append(root.val)
                root=root.right
        return result

"后序遍历是左右根，根据前序遍历左根左右，改一下，然后倒叙输出"

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)
node7=TreeNode(7)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7
result1=Solution().pre(node1)
print(result1)
result2=Solution().inorder(node1)
print(result2)