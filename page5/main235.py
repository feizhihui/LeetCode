# encoding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = self.get_path(root, p)
        path2 = self.get_path(root, q)
        p = 0
        while p < len(path1) and p < len(path2) and path1[p] is path2[p]:
            p += 1
        if p < 1:
            return None
        else:
            return path1[p - 1]

    def get_path(self, root, p):
        path = [root]
        while root:
            path.append(root.val)
            if p.val > root.val:
                root = root.right
            elif p.val < root.val:
                root = root.left
            else:
                break
        return path


if __name__ == '__main__':
    pass
