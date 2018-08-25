"题目：输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。"
"路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)"
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        self.dfs(root,[root.val],result,expectNumber)
        return result
    def dfs(self,root,alist,result,expectNumber):
        if root.left == None and root.right == None:
            if sum(alist)==expectNumber:
                result.append(alist)
        if root.left:
            self.dfs(root.left,alist+[root.left.val],result,expectNumber)
        if root.right:
            self.dfs(root.right,alist+[root.right.val],result,expectNumber)
"深刻理解在dfs中，result随递归而改变，这种写法"
a=TreeNode(10)
b=TreeNode(5)
c=TreeNode(12)
d=TreeNode(4)
e=TreeNode(7)
a.left=b
a.right=c
b.left=d
b.right=e

result=Solution().FindPath(a,22)
print(result)
