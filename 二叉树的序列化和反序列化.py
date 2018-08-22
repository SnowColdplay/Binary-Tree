class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    "先序遍历进行序列化"
    def preorder(self,root,result):
        if root==None:
            result.append("#!")
            return None
        result.extend([str(root.val)+"!"])
        if root.left:
            self.preorder(root.left,result)
        if root.right:
            self.preorder(root.right,result)

    def Serialize(self, root):
        result=[]
        self.preorder(root,result)
        return ",".join(result)

    def Deserialize(self, s):
        valuelist = s.split(',')
        root = self.preorderdes(valuelist)
        return root

    def preorderdes(self, valuelist):
        if len(valuelist) == 0 or valuelist[0] == '':
            return None
        # 遇到#字符，直接删除，返回空结点
        if valuelist[0] == '#':
            del valuelist[0]
            return None
        root = TreeNode(int(valuelist[0]))
        del valuelist[0]
        root.left = self.preorderdes(valuelist)
        root.right = self.preorderdes(valuelist)
        return root


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
result1=Solution().Serialize(node1)
print(result1)
