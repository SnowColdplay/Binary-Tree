class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0:
            return None
        root=TreeNode(pre[0])
        index=tin.index(root.val)
        root.left=self.reConstructBinaryTree(pre[1:index+1],tin[:index])
        root.right=self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return root

result=Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(result.val)
