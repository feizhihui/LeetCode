# encoding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # iteration method
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     queue = [root]
    #     while queue:
    #         vals = [node.val if node != None else None for node in queue]
    #         if vals != vals[::-1]:
    #             return False
    #         queue = [child for node in queue if node for child in (node.left, node.right)]
    #     return True

    # recursive method
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSym(L, R):
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R

        return not root or isSym(root.left, root.right)


if __name__ == '__main__':
    sl = Solution()
    head1 = TreeNode(1)
    head1.left = TreeNode(2)
    head1.right = TreeNode(2)
    ans = sl.isSymmetric(head1)
    print(ans)
