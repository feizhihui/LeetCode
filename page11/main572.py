# encoding=utf-8


def create_tree(plist):
    n = len(plist)
    if n == 0:
        return None
    node_list = [TreeNode(plist[i]) for i in range(n)]
    for i in range(n):
        if 2 * i + 1 < n and plist[2 * i + 1] != None:
            node_list[i].left = node_list[2 * i + 1]
        if 2 * i + 2 < n and plist[2 * i + 2] != None:
            node_list[i].right = node_list[2 * i + 2]
    return node_list[0]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode(as a subtree?)
        :rtype: bool
        """

        if self.sameTree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, t1, t2):
        if not (t1 or t2):  # all false
            return True
        if not (t1 and t2):  # only one false
            return False
        if t1.val == t2.val:
            return self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right)

        return False


if __name__ == '__main__':
    s = create_tree([3, 4, 5, 1, 2])
    t = create_tree([4, 1, 2])
    solu = Solution()

    print(solu.isSubtree(s, t))
