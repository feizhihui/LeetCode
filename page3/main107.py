# encoding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [root]
        ans = []
        while queue:
            vals = [node.val for node in queue]
            queue = [child for node in queue for child in (node.left, node.right) if child]
            ans.append(vals)
        return ans[::-1]


if __name__ == '__main__':
    sl = Solution()
    # head = TreeNode(1)
    # head.left = TreeNode(2)
    # head.right = TreeNode(3)
    print(sl.levelOrderBottom(None))
