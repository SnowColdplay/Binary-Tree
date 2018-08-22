class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def levelorder(self, root):
        result=[]
        level=[root]
        while level:
            level_result=[]
            next_level=[]
            for tmp in level:
                level_result.append(tmp.val)
                if tmp.left:
                    next_level.append(tmp.left)
                if tmp.right:
                    next_level.append(tmp.right)
            result.append(level_result)
            level=next_level
        return result

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
result1=Solution().levelorder(node1)
print(result1)