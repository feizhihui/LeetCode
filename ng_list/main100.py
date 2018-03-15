# encoding=utf-8
from collections import deque


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
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        p_pre = tuple(self.pre_order_dfs(p, []))
        q_pre = tuple(self.pre_order_dfs(q, []))
        if p_pre != q_pre:
            return False

        p_mid = tuple(self.middle_order_dfs(p, []))
        q_mid = tuple(self.middle_order_dfs(q, []))
        print(p_mid)
        print(q_mid)
        if p_mid != q_mid:
            return False

        return True

    def pre_order_dfs(self, p, res):
        if p == None:
            res.append(None)
            return res
        res.append(p.val)
        self.pre_order_dfs(p.left, res)
        self.pre_order_dfs(p.right, res)
        return res

    def middle_order_dfs(self, p, res):
        if p == None:
            res.append(None)
            return res
        self.pre_order_dfs(p.left, res)
        res.append(p.val)
        self.pre_order_dfs(p.right, res)
        return res


if __name__ == '__main__':
    p = create_tree([1, 1])  # 1, 2, 3
    q = create_tree([1, None, 1])  # 1, 2, 3, 4
    s = Solution()
    print(s.isSameTree(p, q))
