"输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同."
"思路：1.后序遍历顺序是 左右根 2.二叉搜索树的性质是 左<根<右"
"1.确定root 2.遍历序列(除去root节点),找到第一个大于root的位置，则该位置左边为左子树，右边为右子树"
"3.遍历右子树，若发现小于root的值，则直接返回fasle"
"4.分别判断左子树和右子树是否仍是二叉搜索时(递归)"
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        index = -1
        for i in range(len(sequence) - 1):
            index = index + 1
            if sequence[i] > root:
                break
        for i in range(index + 1, len(sequence)):
            if sequence[i] < root:
                return False
        left = self.VerifySquenceOfBST(sequence[:index + 1])
        right = self.VerifySquenceOfBST(sequence[index + 1:])

        return left and right



