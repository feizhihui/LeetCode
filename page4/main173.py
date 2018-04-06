# encoding=utf-8


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs_print(root):
    print(root.val)
    if root.left:
        dfs_print(root.left)
    if root.right:
        dfs_print(root.right)


def build_tree(nums):
    n = len(nums)
    if n == 0:
        return None
    nodes = [TreeNode(nums[i]) for i in range(n)]
    for i in range(n):
        nodes[i].left = nodes[2 * i + 1] if 2 * i + 1 < n else None
        nodes[i].right = nodes[2 * i + 2] if 2 * i + 2 < n  else  None
    return nodes[0]


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """

        self.result = self.dfs(root)[::-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.result) > 0

    def next(self):
        """
        :rtype: int
        """
        val = self.result.pop(-1)
        return val

    def dfs(self, root):
        if not root:
            return []
        nums = []
        if root.left:
            nums.extend(self.dfs(root.left))
        nums.append(root.val)
        if root.right:
            nums.extend(self.dfs(root.right))
        return nums


# Your BSTIterator will be called like this:
if __name__ == '__main__':
    nums = [2, 1]
    root = build_tree(nums)


    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    print(v)
