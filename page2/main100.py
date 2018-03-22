# encoding=utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        return self.dfs(p, q)

    def dfs(self, p, q):
        if p.val != q.val:
            return False
        mark = True
        if p.left != None and q.left != None:
            mark = mark & self.dfs(p.left, q.left)
        elif p.left == None and q.left == None:
            pass
        else:
            return False
        if p.right != None and q.right != None:
            mark = mark & self.dfs(p.right, q.right)
        elif p.right == None and q.right == None:
            pass
        else:
            return False
        return mark


if __name__ == '__main__':
    p = create_tree([1, 2, 1])  # 1, 2, 3
    q = create_tree([1, None, 1])  # 1, 2, 3, 4
    s = Solution()
    print(s.isSameTree(p, q))
