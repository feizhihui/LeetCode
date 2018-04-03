# encoding=utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        h1 = self.depth(root.left)
        h2 = self.depth(root.right)
        if abs(h1 - h2) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1




if __name__ == '__main__':
    sl = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    print(sl.depth(head))
    print(sl.isBalanced(head))

