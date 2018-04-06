# encoding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(nums):
    n = len(nums)
    if n == 0:
        return None
    nodes = [TreeNode(nums[i]) for i in range(n)]
    for i in range(n):
        nodes[i].left = nodes[2 * i + 1] if 2 * i + 1 < n else None
        nodes[i].right = nodes[2 * i + 2] if 2 * i + 2 < n else None
    return nodes[0]


def dfs_print(root):
    print(root.val )
    if root.left:
        dfs_print(root.left)
    if root.right:
        dfs_print(root.right)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    root = build_tree(nums)
    dfs_print(root)
