class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    "先序遍历"
    def _pre(self,root,result):
        result.append(root.val)
        if root.left:
            self._pre(root.left,result)
        if root.right:
            self._pre(root.right,result)

    def pre(self,root):
        if root==None:
            return []
        result=[]
        self._pre(root,result)
        return result

    "中序遍历"
    def _inorder(self,root,result):
        if root.left:
            self._inorder(root.left,result)
        result.append(root.val)
        if root.right:
            self._inorder(root.right,result)

    def inorder(self,root):
        if root==None:
            return []
        result=[]
        self._inorder(root,result)
        return result

    "后序遍历"
    def _post(self,root,result):
        if root.left:
            self._post(root.left,result)
        if root.right:
            self._post(root.right,result)
        result.append(root.val)

    def post(self,root):
        if not root:
            return []
        result=[]
        self._post(root,result)
        return result

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node1.left=node2
node1.right=node3
result1=Solution().pre(node1)
print(result1)
result2=Solution().inorder(node1)
print(result2)
result3=Solution().post(node1)
print(result3)